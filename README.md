# 🌦️ Cultural Weather Explorer

**Discover weather-appropriate cultural activities in any location!**

This application combines real-time weather data with local cultural information to suggest the best activities based on current conditions.



## 🌟 Features

- **Weather-aware suggestions**: Get recommendations tailored to current weather conditions
- **Multi-source data**: Combines information from 5 different APIs
- **Beautiful GUI**: Themed interface that adapts to weather conditions
- **Multiple output formats**: Choose between console or graphical interface
- **Smart caching**: Reduces API calls and improves performance

## 🛠️ Technologies Used

- Python 3.8+
- Tkinter (for GUI)
- Pillow (for image handling)
- Requests (for API calls)
- Public APIs:
  - OpenWeatherMap (weather data)
  - Ticketmaster (events)
  - OpenTripMap (attractions)
  - REST Countries (country info)
  - Nominatim (geocoding)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cultural-weather-explorer.git
   cd cultural-weather-explorer
Create and activate a virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up your API keys:

Create a .env file in the project root

Add your API keys:

Copy
OPENWEATHER_API_KEY=your_key_here
TICKETMASTER_API_KEY=your_key_here
OPENTRIPMAP_API_KEY=your_key_here
🚀 Usage
Basic Usage
bash
Copy
python main.py
(Uses your current location)

Specify a Location
bash
Copy
python main.py --location "Paris"
Launch GUI Version
bash
Copy
python main.py --gui
Combine Options
bash
Copy
python main.py --location "New York" --gui
Output Formats
Console (default)

Graphical Interface (--gui flag)

JSON output (for developers)

📂 Project Structure
Copy
cultural_weather_explorer/
├── main.py                # Main application entry point
├── config.py              # Configuration and API keys
├── api_clients/           # API wrapper modules
│   ├── geolocation.py     # Location detection
│   ├── weather.py         # Weather data
│   ├── events.py          # Local events
│   ├── attractions.py     # Tourist attractions
│   └── countries.py       # Country information
├── data_processing/       # Data analysis
│   ├── weather_analyzer.py # Weather categorization
│   └── cultural_matcher.py # Activity suggestions
├── output/                # Output handlers
│   ├── console_output.py  # CLI output
│   └── gui_output.py      # Graphical interface
├── utils/                 # Utilities
│   └── cache.py           # API response caching
├── requirements.txt       # Dependencies
└── README.md              # This file

🎨 GUI Features
Dynamic theming: Changes colors based on weather

Interactive tabs: Browse weather, events, and attractions

Responsive design: Adapts to different screen sizes

Quick links: Direct access to event tickets

Visual weather display: With icons and detailed metrics



✉️ Contact
For questions or support, please contact:

Your Name - your.email@example.com

Project Link: https://github.com/yourusername/cultural-weather-explorer
