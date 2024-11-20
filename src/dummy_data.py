import pandas as pd
import random


def generate_dummy_data():
    # Define possible weather descriptions
    weather_descriptions = [
        "Cerah", "Cerah Berawan", "Berawan", "Berawan Tebal", "Hujan Ringan", "Hujan Sedang", "Hujan Lebat", "Hujan Petir", "Kabut"
    ]

    # Generate 500 records
    num_records = 500

    # Base time for records (already in WIB)
    base_time = pd.Timestamp("2024-01-01 00:00:00")

    data = {
        "Time of Record (WIB)": [
            base_time + pd.Timedelta(hours=i) for i in range(num_records)
        ],
        "Temperature (°C)": [random.uniform(-10, 40) for _ in range(num_records)],
        "Humidity (%)": [random.uniform(10, 100) for _ in range(num_records)],
        "Pressure": [random.uniform(900, 1100) for _ in range(num_records)],
        "Wind Speed (m/s)": [random.uniform(0, 20) for _ in range(num_records)],
        "Weather Description": [random.choice(weather_descriptions) for _ in range(num_records)],
        "AQI (CN)": [random.uniform(10, 200) for _ in range(num_records)],
        "Main Pollutant (CN)": [random.choice(["PM2.5", "PM10", "O3", "NO2", "SO2", "CO"]) for _ in range(num_records)],
        # "Predicted Temperature (°C)": [random.uniform(-10, 40) for _ in range(num_records)],
        # "Predicted Humidity (%)": [random.uniform(10, 100) for _ in range(num_records)],
        # "Predicted Time of Record (WIB)": [
        #     base_time + pd.Timedelta(hours=i + 1) for i in range(num_records)
        # ],
        # "Predicted Weather Description": [random.choice(weather_descriptions) for _ in range(num_records)],
        # "Predicted Wind Speed (m/s)": [random.uniform(0, 20) for _ in range(num_records)],
    }

    return pd.DataFrame(data)

print(generate_dummy_data())