import requests
from utils.cache import cache

class CountriesClient:
    BASE_URL = "https://restcountries.com/v3.1"
    
    @cache(ttl=86400)
    def get_country_info(self, country_code):
        try:
            response = requests.get(f"{self.BASE_URL}/alpha/{country_code}")
            response.raise_for_status()
            data = response.json()[0]
            return {
                'name': data['name'],
                'capital': data.get('capital', ['Unknown']),
                'population': data['population'],
                'languages': data.get('languages', {}),
                'currencies': data.get('currencies', {}),
                'flags': data['flags']
            }
        except requests.RequestException as e:
            print(f"Countries API error: {e}")
            return None