import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> dict:
    if not API_KEY:
        return {"error": "No API key. Add OPENWEATHER_API_KEY to your .env file."}
    try:
        url  = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if resp.status_code != 200:
            return {"error": data.get("message", "City not found")}
        return {
            "temperature": data["main"]["temp"],
            "humidity":    data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "city":        data["name"],
        }
    except Exception as e:
        return {"error": str(e)}
