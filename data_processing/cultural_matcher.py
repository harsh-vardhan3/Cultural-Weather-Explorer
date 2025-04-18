class CulturalMatcher:
    SUGGESTIONS = {
        'temperature': {
            'freezing': ["Visit museums", "Try local cuisine indoors", "See indoor shows"],
            'cold': ["Explore bookstores", "Visit art galleries", "Try coffee shops"],
            'cool': ["Walking tours", "Outdoor markets", "Historical sites"],
            'warm': ["Outdoor dining", "Parks and gardens", "Street art tours"],
            'hot': ["Beach activities", "Water parks", "Early morning sightseeing"]
        },
        'condition': {
            'rainy': ["Museums", "Indoor festivals", "Café hopping"],
            'snowy': ["Winter sports", "Cozy pubs", "Indoor events"],
            'clear': ["Outdoor photography", "Sightseeing", "Rooftop bars"],
            'cloudy': ["Long museum visits", "Factory tours", "Workshops"]
        }
    }
    
    @classmethod
    def generate_suggestions(cls, weather_cat, attractions, events):
        temp_cat, cond_cat = weather_cat
        suggestions = []
        
        suggestions.extend(cls.SUGGESTIONS['temperature'].get(temp_cat, []))
        suggestions.extend(cls.SUGGESTIONS['condition'].get(cond_cat, []))
        
        for attr in attractions[:3]:
            name = attr.get('name', '').lower()
            if 'museum' in name:
                suggestions.append(f"Visit {attr['name']}")
            elif 'park' in name and temp_cat in ['cool', 'warm']:
                suggestions.append(f"Explore {attr['name']}")
        
        return list(set(suggestions))[:5]