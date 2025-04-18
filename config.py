import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
    TICKETMASTER_API_KEY = os.getenv('TICKETMASTER_API_KEY', 'your_api_key_here')
    OPENTRIPMAP_API_KEY = os.getenv('OPENTRIPMAP_API_KEY', 'your_api_key_here')
    
    CACHE_ENABLED = True
    CACHE_DIR = ".cache"
    CACHE_TTL = 3600 