import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io
import requests
import time
import webbrowser
from typing import Dict, Any

class CulturalWeatherGUI:
    """Enhanced graphical user interface with themes for Cultural Weather Explorer"""
    
    THEMES = {
        "light": {
            "bg": "#ffffff",
            "fg": "#333333",
            "accent": "#4a6fa5",
            "secondary": "#e0e0e0"
        },
        "dark": {
            "bg": "#2d2d2d",
            "fg": "#e0e0e0",
            "accent": "#6b98d6",
            "secondary": "#4a4a4a"
        },
        "sunset": {
            "bg": "#f8e8d3",
            "fg": "#553927",
            "accent": "#d96036",
            "secondary": "#eac4a3"
        }
    }
    
    def __init__(self, data: Dict[str, Any]):
        """Initialize the GUI with weather and cultural data"""
        self.root = tk.Tk()
        self.root.title("Cultural Weather Explorer")
        self.root.geometry("950x700")
        self.data = data
        self.theme = self._select_theme_from_weather()
        self._configure_styles()
        self.setup_ui()
    
    def _select_theme_from_weather(self) -> str:
        """Select theme based on weather conditions"""
        if 'weather' not in self.data:
            return "light"
            
        conditions = self.data['weather']['conditions'].lower()
        temp = self.data['weather']['temp']
        
        if 'clear' in conditions:
            return "sunset" if temp > 25 else "light"
        return "dark"
    
    def _configure_styles(self):
        """Configure ttk styles for the selected theme"""
        theme = self.THEMES[self.theme]
        style = ttk.Style()
        style.theme_use('clam')
        
        # Base styles
        style.configure(".", 
                      background=theme["bg"],
                      foreground=theme["fg"],
                      font=('Segoe UI', 10))
        
        # Component styles
        style.configure("TFrame", background=theme["bg"])
        style.configure("TLabel", background=theme["bg"], foreground=theme["fg"])
        style.configure("TButton", background=theme["accent"], foreground="#000000")
        style.configure("TNotebook", background=theme["bg"], tabmargins=[2, 5, 2, 0])
        style.configure("TNotebook.Tab", 
                      background=theme["secondary"],
                      foreground=theme["fg"],
                      padding=[10, 2])
        
        # Style maps
        style.map("TNotebook.Tab",
                background=[("selected", theme["accent"])],
                foreground=[("selected", "#000000")])
        
        self.root.configure(background=theme["bg"])
    
    def setup_ui(self):
        """Setup the main user interface"""
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self._create_top_bar(main_frame)
        self._create_enhanced_weather_display(main_frame)
        
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=15)
        
        # Create tabs
        tabs = [
            ("🏠 Home", self._create_home_tab),
            ("🎭 Events", self._create_events_tab),
            ("🏛️ Attractions", self._create_attractions_tab)
        ]
        
        for tab_text, tab_creator in tabs:
            tab_frame = ttk.Frame(notebook)
            tab_creator(tab_frame)
            notebook.add(tab_frame, text=tab_text)
        
        self._create_status_bar(main_frame)
    
    def _create_top_bar(self, parent):
        """Create the top location bar"""
        theme = self.THEMES[self.theme]
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=(0, 10))
        
        location_text = f"🌍 {self.data['location']['city']}"
        ttk.Label(
            frame, 
            text=location_text,
            font=('Segoe UI', 18, 'bold')
        ).pack(side=tk.LEFT)
        
        # Future: Add refresh/settings buttons here
        controls_frame = ttk.Frame(frame)
        controls_frame.pack(side=tk.RIGHT)
    
    def _create_enhanced_weather_display(self, parent):
        """Create the weather display panel"""
        theme = self.THEMES[self.theme]
        weather_frame = tk.Frame(
            parent, 
            background=theme["accent"],
            highlightthickness=1,
            highlightbackground=theme["secondary"]
        )
        weather_frame.pack(fill=tk.X, pady=10)
        
        # Weather icon
        try:
            icon_url = f"https://openweathermap.org/img/wn/{self.data['weather']['icon']}@2x.png"
            icon_data = requests.get(icon_url).content
            icon_img = Image.open(io.BytesIO(icon_data))
            icon_img = icon_img.resize((100, 100), Image.Resampling.LANCZOS)
            icon_photo = ImageTk.PhotoImage(icon_img)
            
            icon_label = tk.Label(weather_frame, image=icon_photo, background=theme["accent"])
            icon_label.image = icon_photo
            icon_label.pack(side=tk.LEFT, padx=15, pady=10)
        except Exception:
            icon_label = tk.Label(
                weather_frame, 
                text="☁️", 
                font=("Segoe UI", 36),
                background=theme["accent"],
                foreground="#ffffff"
            )
            icon_label.pack(side=tk.LEFT, padx=15, pady=10)
        
        # Weather info
        info_frame = tk.Frame(weather_frame, background=theme["accent"])
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(
            info_frame,
            text=f"{self.data['weather']['temp']}°C | {self.data['weather']['description'].capitalize()}",
            font=('Segoe UI', 14),
            background=theme["accent"],
            foreground="#ffffff"
        ).pack(anchor=tk.W)
        
        # Weather details
        details_frame = tk.Frame(weather_frame, background=theme["accent"])
        details_frame.pack(side=tk.RIGHT, padx=15, pady=10)
        
        for detail in [
            f"💧 Humidity: {self.data['weather']['humidity']}%",
            f"💨 Wind: {self.data['weather']['wind_speed']} m/s"
        ]:
            tk.Label(
                details_frame,
                text=detail,
                font=('Segoe UI', 11),
                background=theme["accent"],
                foreground="#ffffff",
                anchor=tk.W
            ).pack(pady=2)
    
    def _create_home_tab(self, parent):
        """Create the home tab with overview content"""
        theme = self.THEMES[self.theme]
        
        # Scrollable frame setup
        canvas = tk.Canvas(parent, background=theme["bg"])
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Welcome header
        ttk.Label(
            scroll_frame,
            text=f"Welcome to {self.data['location']['city']}!",
            font=('Segoe UI', 16, 'bold'),
            padding="0 10"
        ).pack(anchor=tk.W, fill=tk.X)
        
        ttk.Separator(scroll_frame, orient='horizontal').pack(fill=tk.X, pady=10)
        
        # Activity suggestions
        ttk.Label(
            scroll_frame,
            text="What to do today",
            font=('Segoe UI', 14, 'bold'),
            padding="0 5"
        ).pack(anchor=tk.W, fill=tk.X)
        
        suggestion_frame = ttk.Frame(scroll_frame)
        suggestion_frame.pack(fill=tk.X, pady=10)
        
        for idx, suggestion in enumerate(self.data['suggestions'][:3]):
            card = tk.Frame(
                suggestion_frame,
                background=theme["secondary"],
                padx=10,
                pady=10,
                bd=1,
                relief=tk.RAISED
            )
            card.grid(row=0, column=idx, padx=5, sticky="nsew")
            
            icon = "🎭" if "museum" in suggestion.lower() else (
                  "🏞️" if "park" in suggestion.lower() else (
                  "🍽️" if "dining" in suggestion.lower() else "✨"))
            
            tk.Label(
                card,
                text=icon,
                font=('Segoe UI', 24),
                background=theme["secondary"]
            ).pack()
            
            tk.Label(
                card,
                text=suggestion,
                font=('Segoe UI', 11),
                wraplength=200,
                background=theme["secondary"]
            ).pack(pady=5)
            
            suggestion_frame.grid_columnconfigure(idx, weight=1)
        
        # Highlights section
        ttk.Label(
            scroll_frame,
            text="Highlights",
            font=('Segoe UI', 14, 'bold'),
            padding="0 15 0 5"
        ).pack(anchor=tk.W, fill=tk.X)
        
        highlights_frame = ttk.Frame(scroll_frame)
        highlights_frame.pack(fill=tk.X, pady=5)
        
        if self.data['events']:
            event = self.data['events'][0]
            self._create_highlight_item(
                highlights_frame, 
                title=event['title'],
                subtitle=f"📅 {event['date']} at {event['venue']}",
                icon="🎭"
            ).pack(fill=tk.X, pady=5)
        
        if self.data['attractions']:
            attr = self.data['attractions'][0]
            self._create_highlight_item(
                highlights_frame, 
                title=attr.get('name', 'Local Attraction'),
                subtitle=attr.get('kinds', '').replace(',', ', ').title(),
                icon="🏛️"
            ).pack(fill=tk.X, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _create_events_tab(self, parent):
        """Create the events tab"""
        theme = self.THEMES[self.theme]
        
        ttk.Label(
            parent,
            text="Upcoming Events",
            font=('Segoe UI', 14, 'bold'),
            padding="10"
        ).pack(anchor=tk.W)
        
        # Scrollable events area
        canvas = tk.Canvas(parent, background=theme["bg"])
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        if not self.data['events']:
            ttk.Label(
                scroll_frame,
                text="No events found for this location",
                font=('Segoe UI', 11, 'italic'),
                padding="20"
            ).pack()
        else:
            for event in self.data['events']:
                event_card = tk.Frame(
                    scroll_frame,
                    background=theme["secondary"],
                    padx=15,
                    pady=15,
                    bd=1,
                    relief=tk.RAISED
                )
                event_card.pack(fill=tk.X, padx=10, pady=5)
                
                tk.Label(
                    event_card,
                    text=event['title'],
                    font=('Segoe UI', 12, 'bold'),
                    anchor=tk.W,
                    justify=tk.LEFT,
                    background=theme["secondary"]
                ).pack(anchor=tk.W)
                
                details_frame = tk.Frame(event_card, background=theme["secondary"])
                details_frame.pack(fill=tk.X, pady=(5, 0), anchor=tk.W)
                
                tk.Label(
                    details_frame,
                    text=f"📅 {event['date']}",
                    font=('Segoe UI', 10),
                    background=theme["secondary"]
                ).pack(side=tk.LEFT, padx=(0, 15))
                
                tk.Label(
                    details_frame,
                    text=f"📍 {event['venue']}",
                    font=('Segoe UI', 10),
                    background=theme["secondary"]
                ).pack(side=tk.LEFT)
                
                ttk.Button(
                    event_card,
                    text="Get Tickets",
                    command=lambda url=event['url']: webbrowser.open(url)
                ).pack(anchor=tk.E, pady=(10, 0))
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _create_attractions_tab(self, parent):
        """Create the attractions tab"""
        theme = self.THEMES[self.theme]
        
        ttk.Label(
            parent,
            text="Local Attractions",
            font=('Segoe UI', 14, 'bold'),
            padding="10"
        ).pack(anchor=tk.W)
        
        # Scrollable area
        canvas = tk.Canvas(parent, background=theme["bg"])
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        if not self.data['attractions']:
            ttk.Label(
                scroll_frame,
                text="No attractions found for this location",
                font=('Segoe UI', 11, 'italic'),
                padding="20"
            ).pack()
        else:
            grid_frame = ttk.Frame(scroll_frame)
            grid_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            grid_frame.columnconfigure(0, weight=1)
            grid_frame.columnconfigure(1, weight=1)
            
            for idx, attr in enumerate(self.data['attractions']):
                row, col = divmod(idx, 2)
                
                card = tk.Frame(
                    grid_frame,
                    background=theme["secondary"],
                    padx=15,
                    pady=15,
                    bd=1, 
                    relief=tk.RAISED
                )
                card.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                
                tk.Label(
                    card,
                    text=attr.get('name', 'Local Attraction'),
                    font=('Segoe UI', 12, 'bold'),
                    anchor=tk.W,
                    justify=tk.LEFT,
                    wraplength=350,
                    background=theme["secondary"]
                ).pack(anchor=tk.W)
                
                if 'kinds' in attr:
                    kinds = attr['kinds'].replace(',', ', ').title()
                    tk.Label(
                        card,
                        text=kinds,
                        font=('Segoe UI', 9),
                        anchor=tk.W,
                        justify=tk.LEFT,
                        background=theme["secondary"]
                    ).pack(anchor=tk.W, pady=(5, 0))
                
                if 'wikipedia_extracts' in attr and 'text' in attr['wikipedia_extracts']:
                    desc = attr['wikipedia_extracts']['text']
                    if len(desc) > 200:
                        desc = desc[:200] + "..."
                    
                    tk.Label(
                        card,
                        text=desc,
                        font=('Segoe UI', 10),
                        anchor=tk.W,
                        justify=tk.LEFT,
                        wraplength=350,
                        background=theme["secondary"]
                    ).pack(anchor=tk.W, pady=(10, 0))
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _create_highlight_item(self, parent, title: str, subtitle: str = None, icon: str = None):
        """Helper to create highlight items"""
        theme = self.THEMES[self.theme]
        
        frame = tk.Frame(
            parent,
            background=theme["secondary"],
            padx=10,
            pady=10,
            bd=1,
            relief=tk.RAISED
        )
        
        if icon:
            tk.Label(
                frame,
                text=icon,
                font=('Segoe UI', 18),
                background=theme["secondary"]
            ).pack(side=tk.LEFT, padx=(0, 10))
        
        content_frame = tk.Frame(frame, background=theme["secondary"])
        content_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(
            content_frame,
            text=title,
            font=('Segoe UI', 12, 'bold'),
            anchor=tk.W,
            justify=tk.LEFT,
            background=theme["secondary"]
        ).pack(anchor=tk.W)
        
        if subtitle:
            tk.Label(
                content_frame,
                text=subtitle,
                font=('Segoe UI', 9),
                anchor=tk.W,
                justify=tk.LEFT,
                background=theme["secondary"]
            ).pack(anchor=tk.W)
        
        return frame
    
    def _create_status_bar(self, parent):
        """Create the status bar at bottom"""
        theme = self.THEMES[self.theme]
        
        frame = tk.Frame(
            parent,
            background=theme["secondary"],
            height=25
        )
        frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        tk.Label(
            frame,
            text=f"Data last updated: {time.strftime('%H:%M:%S')}",
            font=('Segoe UI', 8),
            background=theme["secondary"]
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Label(
            frame,
            text="v2.0 Professional",
            font=('Segoe UI', 8),
            background=theme["secondary"]
        ).pack(side=tk.RIGHT, padx=10)
    
    def run(self):
        """Run the GUI main loop"""
        self.root.mainloop()