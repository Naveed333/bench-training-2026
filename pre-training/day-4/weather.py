import sys
import urllib.request
import urllib.parse
import urllib.error
import json

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Icy fog", 51: "Light drizzle", 53: "Moderate drizzle",
    55: "Dense drizzle", 61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow", 80: "Slight showers",
    81: "Moderate showers", 82: "Violent showers", 95: "Thunderstorm",
    96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
}


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "python-script"})
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())


def get_coordinates(city):
    query = urllib.parse.urlencode({"name": city, "count": 1, "language": "en", "format": "json"})
    url = f"https://geocoding-api.open-meteo.com/v1/search?{query}"
    data = fetch_json(url)
    results = data.get("results")
    if not results:
        print(f"Error: City '{city}' not found.")
        return None
    r = results[0]
    return r["latitude"], r["longitude"], r["name"], r.get("country", "")


def get_weather(lat, lon):
    params = urllib.parse.urlencode({
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
    })
    url = f"https://api.open-meteo.com/v1/forecast?{params}"
    return fetch_json(url)


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fetch_weather_cli(city):
    try:
        result = get_coordinates(city)
        print(f"Coordinates for '{city}': {result}")
        if not result:
            return
        lat, lon, name, country = result

        data = get_weather(lat, lon)
        current = data["current"]

        temp_c = current["temperature_2m"]
        temp_f = celsius_to_fahrenheit(temp_c)
        wind = current["wind_speed_10m"]
        code = current["weather_code"]
        description = WEATHER_CODES.get(code, "Unknown")

        print("\n" + "=" * 40)
        print(f"  Weather for {name}, {country}")
        print("=" * 40)
        print(f"  Description : {description}")
        print(f"  Temperature : {temp_c}°C  /  {temp_f:.1f}°F")
        print(f"  Wind Speed  : {wind} km/h")
        print()

    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
    except (KeyError, ValueError) as e:
        print(f"Error parsing weather data: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    city = " ".join(sys.argv[1:])
    fetch_weather_cli(city)
