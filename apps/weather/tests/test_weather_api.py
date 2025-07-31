import pytest
from rest_framework.test import APIClient

from apps.weather.tests.fixtures.weather_fixtures import weather_entry, weather_entry_creation_response

@pytest.mark.django_db
def test_weather_entry_success_creation_api(mocker, weather_entry_creation_response):
    mocker_weather_api_create = mocker.patch('apps.weather.viewsets.weather_viewset.WeatherEntryViewSet.create')
    mocker_weather_api_create.return_value = weather_entry_creation_response
    
    client = APIClient()
    response = client.post('/weather/', {
        'city': 'São Paulo',
        'state': 'SP',
        'country': 'Brasil'
    })

    assert response.status_code == 201


@pytest.mark.django_db
def test_weather_entry_fail_api_invalid_fields():
    client = APIClient()
    response = client.post('/weather/', {
        'city': '',
        'state': '',
        'country': ''
    })

    assert response.status_code == 400
    assert response.data == {'detail': 'Campos \'city\', \'state\' e \'country\' são obrigatórios.'}


@pytest.mark.django_db
def test_weather_entry_success_list_api(weather_entry):
    client = APIClient()
    response = client.get('/weather/')
    
    assert response.status_code == 200
    assert len(response.data) > 0

