from django.core.cache import cache
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.weather.models import WeatherEntry
from apps.weather.serializers import WeatherEntrySerializer
from apps.weather.serializers.create_weather_entry_serializer import CreateWeatherEntrySerializer, CreateWeatherEntrySerializerError400
from apps.weather.services.openweather_service import OpenWeatherService
import structlog

logger = structlog.get_logger()

class WeatherEntryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = WeatherEntry.objects.all().order_by('-created_at')
    serializer_class = WeatherEntrySerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'weather'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            return queryset[:10]
        
        return queryset

    @swagger_auto_schema(
        request_body=CreateWeatherEntrySerializer,
        responses={
            201: WeatherEntrySerializer, 
            400: openapi.Response(description="Dados não encontrados para a cidade especificada.")
        }
    )
    def create(self, request, *args, **kwargs):
        body = request.data
        city = body.get('city')
        state = body.get('state')
        country = body.get('country')

        if not all([city, state, country]):
            return Response(
                {"detail": "Campos 'city', 'state' e 'country' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Gera chave do cache
        cache_key = f"weather:{city.lower()},{state.lower()},{country.lower()}"

        # Verifica cache
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        
        openweather_service = OpenWeatherService(body)
        weather_data = openweather_service.get_weather()

        if weather_data is None:
            return Response({"error": "Dados não encontrados para a cidade especificada."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = WeatherEntrySerializer(data={
            'city': body['city'],
            'state': body['state'],
            'country': body['country'],
            'latitude': weather_data['coord']['lat'],
            'longitude': weather_data['coord']['lon'],
            'response_data': weather_data
        })
        if serializer.is_valid():
            serializer.save()
            cache.set(cache_key, serializer.data, timeout=600)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
