import streamlit as st
from data_processing import load_data, filter_data
from visualizations import (
    plot_aqi_trend,
    plot_aqi_distribution_by_weather,
    plot_main_pollutant_by_weather,
    plot_weather_aqi_correlation,
)

# Load data
data = load_data()

# Sidebar
st.sidebar.title("Weather and Air Quality Dashboard")
insight = st.sidebar.radio(
    "Select Insight", 
    ["AQI Trend Over Time", 
     "AQI Distribution by Weather Condition", 
     "Main Pollutants by Weather Condition", 
     "Correlation Between Weather Parameters and AQI"]
)

start_date = st.sidebar.date_input("Start Date (WIB)", data['datetime_wib'].min().date())
end_date = st.sidebar.date_input("End Date (WIB)", data['datetime_wib'].max().date())

# Filter data based on date (WIB)
filtered_data = filter_data(data, start_date, end_date)

# Main Content
st.title("Weather and Air Quality Dashboard")

if insight == "AQI Trend Over Time":
    st.pyplot(plot_aqi_trend(filtered_data))
elif insight == "AQI Distribution by Weather Condition":
    st.pyplot(plot_aqi_distribution_by_weather(filtered_data))
elif insight == "Main Pollutants by Weather Condition":
    st.pyplot(plot_main_pollutant_by_weather(filtered_data))
elif insight == "Correlation Between Weather Parameters and AQI":
    st.pyplot(plot_weather_aqi_correlation(filtered_data))
