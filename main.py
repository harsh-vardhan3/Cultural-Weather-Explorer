import argparse
from api_clients import (
    GeolocationClient,
    GeocodingClient,
    WeatherClient,
    EventsClient,
    AttractionsClient,
    CountriesClient
)
from data_processing import WeatherAnalyzer, CulturalMatcher
from output import ConsoleOutput, CulturalWeatherGUI

def main():
    # Initialize all clients
    geo_client = GeolocationClient()
    geocode_client = GeocodingClient()
    weather_client = WeatherClient()
    events_client = EventsClient()
    attractions_client = AttractionsClient()
    countries_client = CountriesClient()

    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Cultural Weather Explorer")
    parser.add_argument("--location", help="City or address to analyze")
    parser.add_argument("--gui", action="store_true", help="Launch GUI interface")
    args = parser.parse_args()

    # Get location data
    if args.location:
        location_data = geocode_client.get_coordinates(args.location)
    else:
        location_data = geo_client.get_location()
    
    if not location_data:
        print("Error: Could not determine location")
        return

    # Fetch all data
    data = {
        'weather': weather_client.get_weather(location_data['lat'], location_data['lon']),
        'events': events_client.get_events(location_data['city'], location_data.get('countryCode', 'us')),
        'attractions': attractions_client.get_attractions(location_data['lat'], location_data['lon']),
        'country': countries_client.get_country_info(location_data.get('countryCode', 'us'))
    }

    # Process data
    weather_cat = WeatherAnalyzer.get_weather_category(data['weather'])
    suggestions = CulturalMatcher.generate_suggestions(
        weather_cat,
        data['attractions'],
        data['events']
    )

    # Prepare output
    output = {
        'location': {
            'city': location_data['city'],
            'country': data['country']['name']['common'] if data['country'] else 'Unknown'
        },
        'weather': data['weather'],
        'events': data['events'],
        'attractions': data['attractions'],
        'suggestions': suggestions
    }

    # Display results
    if args.gui:
        CulturalWeatherGUI(output).run()
    else:
        ConsoleOutput.display(output)

if __name__ == "__main__":
    main()