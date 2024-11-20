import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fungsi untuk koneksi ke PostgreSQL
def get_postgresql_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),  
        port=os.getenv("DB_PORT"),  
        database=os.getenv("DB_NAME"), 
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"), 
        sslmode=os.getenv("DB_SSLMODE", "require")  # Default ke "require" jika tidak ada di .env
    )

# Fungsi untuk mengambil data dari PostgreSQL
def fetch_data(query):
    conn = get_postgresql_connection()
    try:
        # Gunakan pandas untuk membaca query ke dalam DataFrame
        df = pd.read_sql_query(query, conn)
    finally:
        # Tutup koneksi setelah digunakan
        conn.close()
    return df


# # SQL query to fetch the required data
# query = """
# SELECT 
#     time_of_record_wib AS "Time of Record (WIB)",
#     temperature_c AS "Temperature (°C)",
#     humidity_percent AS "Humidity (%)",
#     pressure_hpa AS "Pressure",
#     wind_speed_ms AS "Wind Speed (m/s)",
#     weather_description AS "Weather Description",
#     aqi_cn AS "AQI (CN)",
#     main_pollutant_cn AS "Main Pollutant (CN)"
# FROM weather_pollution_predictions
# ORDER BY time_of_record_wib ASC
# """

# data = fetch_data(query)

# print(data)
