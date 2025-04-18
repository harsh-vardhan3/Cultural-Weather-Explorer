import requests
from utils.cache import cache
from config import Config

class EventsClient:
    BASE_URL = "https://app.ticketmaster.com/discovery/v2/events.json"
    
    @cache(ttl=3600)  # Cache for 1 hour
    def get_events(self, location_name, country_code):
        """Get events for a location"""
        params = {
            "apikey": Config.TICKETMASTER_API_KEY,
            "city": location_name,
            "countryCode": country_code,
            "size": 5
        }
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Handle empty or invalid responses
            if not data.get('_embedded', {}).get('events'):
                return []
                
            events = []
            for event in data['_embedded']['events']:
                # Safely extract venue name
                venue = event.get('_embedded', {}).get('venues', [{}])[0].get('name', 'Unknown venue')
                
                events.append({
                    'title': event.get('name', 'Unknown event'),
                    'date': event.get('dates', {}).get('start', {}).get('localDate', 'Date not available'),
                    'venue': venue,
                    'url': event.get('url', '#')
                })
            return events
            
        except requests.RequestException as e:
            print(f"Events API error: {e}")
            return []
        except (KeyError, ValueError) as e:
            print(f"Error parsing events data: {e}")
            return []