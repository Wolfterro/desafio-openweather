import pytest
from apps.weather.models import WeatherEntry
from apps.weather.tests.fixtures.weather_fixtures import weather_entry

@pytest.mark.django_db
def test_temperature_celsius(weather_entry):
    expected = {
        'min': 295 - 273.15,
        'max': 305 - 273.15,
        'temp': 300 - 273.15,
        'feels_like': 298 - 273.15
    }

    assert weather_entry.temperature_celsius == pytest.approx(expected, rel=1e-2)

@pytest.mark.django_db
def test_temperature_fahrenheit(weather_entry):
    expected = {
        'min': (295 - 273.15) * 1.8 + 32,
        'max': (305 - 273.15) * 1.8 + 32,
        'temp': (300 - 273.15) * 1.8 + 32,
        'feels_like': (298 - 273.15) * 1.8 + 32
    }

    assert weather_entry.temperature_fahrenheit == pytest.approx(expected, rel=1e-2)
