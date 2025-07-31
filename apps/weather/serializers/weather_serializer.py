from rest_framework import serializers
from apps.weather.models import WeatherEntry

class WeatherEntrySerializer(serializers.ModelSerializer):
    temperature = serializers.ReadOnlyField()
    temperature_celsius = serializers.ReadOnlyField()
    temperature_fahrenheit = serializers.ReadOnlyField()
    weather_description = serializers.ReadOnlyField()
    weather = serializers.ReadOnlyField()
    icon_url = serializers.ReadOnlyField()
    pressure = serializers.ReadOnlyField()
    humidity = serializers.ReadOnlyField()
    wind_speed = serializers.ReadOnlyField()
    wind_direction = serializers.ReadOnlyField()
    visibility = serializers.ReadOnlyField()

    class Meta:
        model = WeatherEntry
        fields = [
            'id', 'city', 'state', 'country', 'latitude', 'longitude', 'created_at',
            'response_data', 'temperature', 'temperature_celsius', 'temperature_fahrenheit',
            'weather_description', 'weather', 'icon_url',
            'pressure', 'humidity', 'wind_speed', 'wind_direction', 'visibility',
        ]
