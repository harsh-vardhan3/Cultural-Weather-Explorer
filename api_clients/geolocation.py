import requests
from config import Config

class GeolocationClient:
    BASE_URL = "http://ip-api.com/json/"
    
    def get_location(self, ip_address=None):
        try:
            response = requests.get(
                self.BASE_URL + (ip_address or ""),
                params={"fields": "city,country,countryCode,lat,lon"},
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Geolocation error: {e}")
            return None