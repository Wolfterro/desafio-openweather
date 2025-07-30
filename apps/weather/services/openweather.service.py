import os

import requests

class OpenWeatherService(object):
    def __init__(self, search_data):
        self.api_key = os.getenv("OW_API_KEY")
        self.base_url = os.getenv("OW_BASE_URL")
        self.search_data = search_data
    
    def get_weather(self):
        lat, lon = self.__get_lat_lon_from_search_data()
        url = f"{self.base_url}?lat={lat}&lon={lon}&appid={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()

            return data
        except Exception as e:
            data = {"error": str(e)}
            return None
    
    # Private methods
    # ---------------
    def __get_lat_lon_from_search_data(self):
        search_params = f"city={self.search_data['city']}&state={self.search_data['state']}&country={self.search_data['country']}"
        url = f"{self.base_url}/geo/1.0/direct?{search_params}&limit=1&appid={self.api_key}"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return None

            data = response.json()
            return data[0]['lat'], data[0]['lon']
        except Exception as e:
            data = {"error": str(e)}
            return None