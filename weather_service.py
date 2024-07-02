import requests

class WeatherService:
    ''' возвращает погоду по указанному городу'''
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, location):
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={location}")
        return response.json()
