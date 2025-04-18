import requests
from config import Config

class GeocodingClient:
    BASE_URL = "https://nominatim.openstreetmap.org/search"
    
    def get_coordinates(self, location_query):
        params = {
            'q': location_query,
            'format': 'json',
            'limit': 1
        }
        headers = {
            'User-Agent': 'CulturalWeatherExplorer/1.0 (contact@example.com)'
        }
        try:
            response = requests.get(
                self.BASE_URL,
                params=params,
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            results = response.json()
            if results:
                return {
                    'city': results[0].get('display_name', '').split(',')[0],
                    'lat': float(results[0]['lat']),
                    'lon': float(results[0]['lon']),
                    'countryCode': results[0].get('address', {}).get('country_code', 'us')
                }
            return None
        except Exception as e:
            print(f"Geocoding error: {e}")
            return None