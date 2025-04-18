class ConsoleOutput:
    @staticmethod
    def display(data):
        print(f"\n🌍 {data['location']['city']}, {data['location']['country']}")
        print(f"🌤️ {data['weather']['description']}, {data['weather']['temp']}°C")
        
        print("\n🎭 Top Events:")
        for event in data['events'][:3]:
            print(f"- {event['title']} at {event['venue']}")
            
        print("\n🏛️ Top Attractions:")
        for attr in data['attractions'][:3]:
            print(f"- {attr.get('name', 'Attraction')}")
            
        print("\n💡 Suggestions:")
        for sug in data['suggestions']:
            print(f"- {sug}")