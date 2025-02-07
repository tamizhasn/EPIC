import os
from kivy.config import Config

random_text = {"Cool, I'm on it sir","okay sir I'm working on it","Just a Second sir"}

width, height = 1920, 1080

Config.set('graphics','width',width)
Config.set('graphics','height',height)
Config.set('graphics','fullscreen','True')

EMAIL = os.environ.get("jarvisvui@gmail.com")
PASSWORD = os.environ.get("Jarvis123")

IP_ADDR_API_URL = os.environ.get("IP_ADDR_API_URL")
NEWS_FETCH_API_URL = os.environ.get("NEWS_FETCH_API_URL")
NEWS_FETCH_API_KEY = os.environ.get("NEWS_FETCH_API_KEY")
WEATHER_FORECAST_API_URL = os.environ.get("WEATHER_FORECAST_API_URL")
WEATHER_FORECAST_API_KEY = os.environ.get("WEATHER_FORECAST_API_KEY")
GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")


SMTP_URL = os.environ.get("SMTP_URL")
SMTP_PORT = os.environ.get("SMTP_PORT")

SCREEN_WIDTH = Config.getint('graphics','width')
SCREEN_HEIGHT = Config.getint('graphics','height')