import psycopg2
import pandas as pd

# Fungsi untuk koneksi ke PostgreSQL
def get_postgresql_connection():
    return psycopg2.connect(
        host="",  
        port="",  
        database="", 
        user="",
        password="", 
        sslmode=""  # Aiven biasanya membutuhkan koneksi SSL
    )

# Fungsi untuk mengambil data dari PostgreSQL
def fetch_data(query):
    conn = get_postgresql_connection()
    try:
        df = pd.read_sql_query(query, conn)
    finally:
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
