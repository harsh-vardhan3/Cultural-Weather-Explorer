class WeatherAnalyzer:
    @staticmethod
    def get_weather_category(weather_data):
        temp = weather_data['temp']
        conditions = weather_data['conditions'].lower()
        
        temp_cat = (
            'freezing' if temp < 0 else
            'cold' if temp < 10 else
            'cool' if temp < 20 else
            'warm' if temp < 30 else
            'hot'
        )
        
        cond_cat = (
            'rainy' if 'rain' in conditions else
            'snowy' if 'snow' in conditions else
            'clear' if 'clear' in conditions else
            'cloudy' if 'cloud' in conditions else
            'other'
        )
        
        return temp_cat, cond_cat
    
    @staticmethod
    def get_weather_icon(icon_code):
        return f"https://openweathermap.org/img/wn/{icon_code}@2x.png"