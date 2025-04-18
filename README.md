# 🌦️ Cultural Weather Explorer

**Discover weather-appropriate cultural activities in any location!**

This application combines real-time weather data with local cultural information to suggest the best activities based on current conditions.

![image](https://github.com/user-attachments/assets/fba282bb-9ee9-473c-a7e1-df843366d3a5)
*

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
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API keys:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     OPENWEATHER_API_KEY=your_key_here
     TICKETMASTER_API_KEY=your_key_here
     OPENTRIPMAP_API_KEY=your_key_here
     ```

## 🚀 Usage

### Basic Usage
```bash
python main.py
```
(Uses your current location)

### Specify a Location
```bash
python main.py --location "Paris"
```

### Launch GUI Version
```bash
python main.py --gui
```

### Combine Options
```bash
python main.py --location "New York" --gui
```

### Output Formats
- Console (default)
- Graphical Interface (--gui flag)
- JSON output (for developers)

## 📂 Project Structure
```
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
```

## 🎨 GUI Features
- Dynamic theming: Changes colors based on weather
- Interactive tabs: Browse weather, events, and attractions
- Responsive design: Adapts to different screen sizes
- Quick links: Direct access to event tickets
- Visual weather display: With icons and detailed metrics

