import requests
from utils.cache import cache
from config import Config

class AttractionsClient:
    BASE_URL = "https://api.opentripmap.com/0.1/en/places/radius"
    DETAILS_URL = "https://api.opentripmap.com/0.1/en/places/xid/{}"
    
    @cache(ttl=86400)
    def get_attractions(self, lat, lon, radius=5000):
        params = {
            'apikey': Config.OPENTRIPMAP_API_KEY,
            'radius': radius,
            'lon': lon,
            'lat': lat,
            'format': 'json',
            'limit': 5
        }
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            places = response.json()
            return [self._get_place_details(place['xid']) for place in places]
        except requests.RequestException as e:
            print(f"Attractions API error: {e}")
            return []
    
    def _get_place_details(self, xid):
        try:
            response = requests.get(self.DETAILS_URL.format(xid), 
                                  params={'apikey': Config.OPENTRIPMAP_API_KEY})
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return {'name': 'Unknown attraction', 'xid': xid}