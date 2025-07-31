import os

import requests
import urllib

class OpenWeatherService(object):
    def __init__(self, search_data):
        self.api_key = os.getenv("OW_API_KEY")
        self.base_url = os.getenv("OW_BASE_URL")
        self.search_data = search_data
    
    def get_weather(self):
        lat, lon = self.get_lat_lon_from_search_data()
        url = f"{self.base_url}/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            if 'cod' in data and data['cod'] != 200:
                return None

            return data
        except Exception as e:
            data = {"error": str(e)} # TODO: Adicionar logs estruturados
            return None

    def get_lat_lon_from_search_data(self):
        search_data = {
            'city': urllib.parse.quote_plus(self.search_data['city']),
            'state': urllib.parse.quote_plus(self.search_data['state']),
            'country': urllib.parse.quote_plus(self.search_data['country'])
        }
        query_params = f"q={search_data['city']},{search_data['state']},{search_data['country']}"
        url = f"{self.base_url}/geo/1.0/direct?{query_params}&limit=1&appid={self.api_key}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                return (None, None)

            data = response.json()
            return (data[0]['lat'], data[0]['lon'])
        except Exception as e:
            data = {"error": str(e)}  # TODO: Adicionar logs estruturados
            return (None, None)