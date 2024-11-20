# Interactive Air Quality Dashboard with Streamlit

## Introduction

This project is an interactive dashboard built with Streamlit to analyze air quality in Yogyakarta, Indonesia. By integrating data from multiple APIs and storing it in a PostgreSQL database, the dashboard provides insights into how weather conditions affect the Air Quality Index (AQI).

## Key Insights

The dashboard includes the following features:

1. **Air Quality Distribution by Weather**  
   Understand how AQI levels vary under different weather conditions.

2. **Main Pollutants by Weather Description**  
   Identify dominant pollutants for each weather condition.

3. **Correlation Between Weather Parameters and AQI**  
   Analyze relationships between temperature, humidity, wind speed, and AQI.

4. **AQI Predictions**  
   Get forecasts of AQI trends based on historical data and weather conditions.

## Setup Instructions

### Prerequisites

- **Python 3.7+**
- **PostgreSQL database** (cloud-hosted, e.g., Aiven)

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:eben4ya/ETL-Streamlit.git
   cd ETL-Streamlit
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the PostgreSQL connection in `app.py`:
   ```python
   def get_postgresql_connection():
       return psycopg2.connect(
           host="YOUR_HOST",
           port="YOUR_PORT",
           database="YOUR_DATABASE",
           user="YOUR_USERNAME",
           password="YOUR_PASSWORD",
           sslmode="require"
       )
   ```

4. Run the dashboard:
   ```bash
   streamlit run app.py
   ```

Access the dashboard at `http://localhost:8501`.

---

## Features

1. **Overview**  
   - Displays key metrics, such as AQI trends and weather summaries.

2. **Interactive Filters**  
   - Filter data by weather conditions or specific pollutants.

3. **Visualizations**  
   - Charts for AQI distribution, main pollutants, and weather correlations.

4. **Data Table**  
   - View raw data directly from the PostgreSQL database.

---

## References

- Project Repository: [GitHub - ETL Air Quality](https://github.com/eben4ya/ETL-air-quality)
- **APIs Used**:
  - [AirVisual API](https://api-docs.iqair.com/)
  - [OpenWeather API](https://openweathermap.org/api)
  - [BMKG API](https://data.bmkg.go.id/)

---

## Member

1. Benaya Imanuela (22/494790/TK/54313)
2. Muhammad Hilmi Dzaki Wismadi (22/497591/TK/54539)
3. Yitzhak Edmund Tio Manalu (22/499769/TK/54763)

## Link
1. Blog Post at [Notion](https://lying-shrine-78d.notion.site/Polusi-Udara-Data-Engineering-1350238f73218085a93dcf8ca0873e4c?pvs=4).
2. Demo Video at [Gdrive](https://drive.google.com/file/d/10bC4HO3JJMpiwpzxx9j9LijChUc5d593/view?usp=sharing)