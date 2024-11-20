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
        sslmode=os.getenv("DB_SSLMODE")
    )

# Fungsi untuk mengambil data dari PostgreSQL
def fetch_data(query):
    conn = get_postgresql_connection()
    try:
        df = pd.read_sql_query(query, conn)
    finally:
        conn.close()
    return df



