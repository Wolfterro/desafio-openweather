from django.core.cache import cache
from rest_framework import viewsets
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from apps.weather.models import WeatherEntry
from apps.weather.serializers import WeatherEntrySerializer
from apps.weather.services.openweather_service import OpenWeatherService

class WeatherEntryViewSet(viewsets.ModelViewSet):
    queryset = WeatherEntry.objects.all().order_by('-created_at')
    serializer_class = WeatherEntrySerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'weather'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            return queryset[:10]
        
        return queryset

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

        print(weather_data)

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
