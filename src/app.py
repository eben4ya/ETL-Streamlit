import streamlit as st
import numpy as np
import pandas as pd

from data_processing import filter_data, calculate_regression_coefficients, predict_aqi
from visualizations import (
    plot_aqi_trend,
    plot_aqi_distribution_by_weather_desc,
    plot_main_pollutant_by_weather_desc,
    plot_weather_aqi_correlation,
    plot_aqi_predictions
)
from data_aiven import fetch_data

# Load data
# SQL query to fetch the required data
query = """
SELECT 
    time_of_record_wib AS "Time of Record (WIB)",
    temperature_c AS "Temperature (°C)",
    humidity_percent AS "Humidity (%)",
    pressure_hpa AS "Pressure",
    wind_speed_ms AS "Wind Speed (m/s)",
    weather_description AS "Weather Description",
    aqi_cn AS "AQI (CN)",
    main_pollutant_cn AS "Main Pollutant (CN)"
FROM weather_pollution_predictions
ORDER BY time_of_record_wib ASC
"""
data = fetch_data(query)

# data.to_csv('data.csv', index=False)

# Sidebar
st.sidebar.title("Weather and Air Quality Dashboard")
insight = st.sidebar.radio(
    "Select Insight",
    ["AQI Trend Over Time",
     "AQI Distribution by Weather Description",
     "Main Pollutants by Weather Description",
     "Correlation Between Weather Parameters and AQI",
     "AQI Predictions"
     ]
)

# Show date inputs for all insights except "AQI Predictions"
if insight != "AQI Predictions":
    start_date = st.sidebar.date_input(
        "Start Date (WIB)", data['Time of Record (WIB)'].min().date())
    end_date = st.sidebar.date_input(
        "End Date (WIB)", data['Time of Record (WIB)'].max().date())
    # Filter data based on date (WIB)
    filtered_data = filter_data(data, start_date, end_date)
else:
    filtered_data = data  # Use all data for predictions

# Show slider for the number of days only when "AQI Predictions" is selected
if insight == "AQI Predictions":
    days = st.sidebar.slider("Select number of days (1-10):",
                             min_value=1, max_value=10, value=5)

# Main Content
st.title("Weather and Air Quality Dashboard")

if insight == "AQI Trend Over Time":
    st.pyplot(plot_aqi_trend(filtered_data))
elif insight == "AQI Distribution by Weather Description":
    st.pyplot(plot_aqi_distribution_by_weather_desc(filtered_data))
elif insight == "Main Pollutants by Weather Description":
    st.pyplot(plot_main_pollutant_by_weather_desc(filtered_data))
elif insight == "Correlation Between Weather Parameters and AQI":
    st.pyplot(plot_weather_aqi_correlation(filtered_data))
elif insight == "AQI Predictions":
    st.subheader("Predict AQI Based on Weather Conditions")

    # Calculate regression coefficients
    coefficients = calculate_regression_coefficients(filtered_data)

    # Generate dummy input for the next 'days' days (e.g., average weather conditions)
    avg_weather = filtered_data[[
        'Temperature (°C)', 'Humidity (%)', 'Pressure', 'Wind Speed (m/s)']].mean().values
    # Repeat the averages for the number of days
    input_data = np.tile(avg_weather, (days, 1))

    # Predict AQI
    predictions = predict_aqi(coefficients, input_data)

    # Display predictions
    st.pyplot(plot_aqi_predictions(predictions, days))

    # Display prediction data in a table
    prediction_table = pd.DataFrame({
        "Day": range(1, days + 1),
        "Predicted AQI": predictions
    })
    st.write(prediction_table)
