import requests
from config import Config

class WeatherClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, lat, lon):
        try:
            response = requests.get(
                self.BASE_URL,
                params={
                    'lat': lat,
                    'lon': lon,
                    'appid': Config.OPENWEATHER_API_KEY,
                    'units': 'metric'
                },
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            return {
                'temp': data['main']['temp'],
                'conditions': data['weather'][0]['main'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
        except Exception as e:
            print(f"Weather API error: {e}")
            return None