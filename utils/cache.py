import os
import json
import time
import hashlib
from functools import wraps
from config import Config

def cache(ttl=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not Config.CACHE_ENABLED:
                return func(*args, **kwargs)
                
            # Create cache dir if not exists
            os.makedirs(Config.CACHE_DIR, exist_ok=True)
            
            # Generate safe cache key using hash
            args_key = str(args[1:]) + str(kwargs)  # Skip self/cls parameter
            cache_key = hashlib.md5(args_key.encode()).hexdigest()
            cache_file = os.path.join(Config.CACHE_DIR, f"{func.__name__}_{cache_key}.json")
            
            # Check cache
            if os.path.exists(cache_file):
                with open(cache_file, 'r') as f:
                    try:
                        data = json.load(f)
                        if time.time() - data['timestamp'] < ttl:
                            return data['result']
                    except (json.JSONDecodeError, KeyError):
                        pass  # Cache file corrupted, regenerate
            
            # Call function if cache miss
            result = func(*args, **kwargs)
            
            # Save to cache
            if result is not None:
                with open(cache_file, 'w') as f:
                    json.dump({
                        'timestamp': time.time(),
                        'result': result
                    }, f)
            
            return result
        return wrapper
    return decorator