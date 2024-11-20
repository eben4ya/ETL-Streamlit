import pandas as pd
import random
import pytz

def generate_dummy_data():
    # Jakarta timezone
    jakarta_tz = pytz.timezone("Asia/Jakarta")
    
    # Define possible weather descriptions
    weather_descriptions = [
        "Clear", "Cloudy", "Partly Cloudy", "Rainy", "Stormy", "Foggy", "Snowy", "Windy", "Hazy", "Thunderstorm"
    ]
    
    data = {
        "measurement_id": range(1, 501),
        "location_id": [random.randint(1, 20) for _ in range(500)],
        "datetime_wib": [
            pd.Timestamp("2024-01-01").tz_localize("UTC").tz_convert(jakarta_tz) + pd.Timedelta(hours=i)
            for i in range(500)
        ],
        "aqi": [random.uniform(10, 200) for _ in range(500)],
        "main_pollutant": [random.choice(["PM2.5", "PM10", "O3", "NO2", "SO2", "CO"]) for _ in range(500)],
        "weather_condition_id": [random.randint(1, 10) for _ in range(500)],
        "weather_desc": [random.choice(weather_descriptions) for _ in range(500)],  # New field
        "temperature_c": [random.uniform(-10, 40) for _ in range(500)],
        "humidity_percent": [random.uniform(10, 100) for _ in range(500)],
        "pressure_hpa": [random.uniform(900, 1100) for _ in range(500)],
        "wind_speed_ms": [random.uniform(0, 20) for _ in range(500)],
        "wind_direction_deg": [random.uniform(0, 360) for _ in range(500)],
        "cloud_coverage_percent": [random.uniform(0, 100) for _ in range(500)],
        "visibility_km": [random.uniform(1, 50) for _ in range(500)],
        "source": [random.choice(["AirVisual", "OpenAQ"]) for _ in range(500)],
    }
    return pd.DataFrame(data)
