from django.db import models

# Create your models here.
# ------------------------
class WeatherEntry(models.Model):
    # Search informations
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    # Response data
    response_data = models.JSONField()
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {self.city}, {self.state} - {self.country}"

    class Meta:
        verbose_name = "Weather Entry"
        verbose_name_plural = "Weather Entries"
    
    # Properties
    @property
    def temperature(self):
        return {
            'min': self.response_data['main']['temp_min'],
            'max': self.response_data['main']['temp_max'],
            'temp': self.response_data['main']['temp'],
            'feels_like': self.response_data['main']['feels_like']
        }
    
    @property
    def temperature_celsius(self):
        return {
            'min': self.temperature['min'] - 273.15,
            'max': self.temperature['max'] - 273.15,
            'temp': self.temperature['temp'] - 273.15,
            'feels_like': self.temperature['feels_like'] - 273.15
        }
    
    @property
    def temperature_fahrenheit(self):
        return {
            'min': (self.temperature['min'] - 273.15) * 1.8 + 32,
            'max': (self.temperature['max'] - 273.15) * 1.8 + 32,
            'temp': (self.temperature['temp'] - 273.15) * 1.8 + 32,
            'feels_like': (self.temperature['feels_like'] - 273.15) * 1.8 + 32
        }
    
    @property
    def weather_description(self):
        if len(self.response_data['weather']) == 0:
            return None

        return self.response_data['weather'][0]['description']
    
    @property
    def weather(self):
        if len(self.response_data['weather']) == 0:
            return None

        return self.response_data['weather'][0]['main']
    
    @property
    def icon_url(self):
        if len(self.response_data['weather']) == 0:
            return None

        return f"https://openweathermap.org/img/wn/{self.response_data['weather'][0]['icon']}@2x.png"

    @property
    def pressure(self):
        return self.response_data['main']['pressure']
    
    @property
    def humidity(self):
        return self.response_data['main']['humidity']
    
    @property
    def wind_speed(self):
        return self.response_data['wind']['speed']
    
    @property
    def wind_direction(self):
        return self.response_data['wind']['deg']
    
    @property
    def visibility(self):
        return self.response_data['visibility']

