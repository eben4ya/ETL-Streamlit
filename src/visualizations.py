import matplotlib.pyplot as plt
import pandas as pd

def plot_aqi_trend(data):
    fig, ax = plt.subplots()
    data.groupby(data['datetime_wib'].dt.date)['aqi'].mean().plot(ax=ax)
    ax.set_title("AQI Trend Over Time (WIB)")
    ax.set_xlabel("Date (WIB)")
    ax.set_ylabel("Average AQI")
    return fig

def plot_aqi_distribution_by_weather(data):
    fig, ax = plt.subplots()
    data.boxplot(column='aqi', by='weather_condition_id', ax=ax)
    ax.set_title("AQI Distribution by Weather Condition")
    ax.set_xlabel("Weather Condition")
    ax.set_ylabel("AQI")
    return fig

def plot_main_pollutant_by_weather(data):
    fig, ax = plt.subplots()
    data.groupby('weather_condition_id')['main_pollutant'].value_counts().unstack().plot(kind='bar', stacked=True, ax=ax)
    ax.set_title("Main Pollutants by Weather Condition")
    ax.set_xlabel("Weather Condition")
    ax.set_ylabel("Count")
    return fig

def plot_weather_aqi_correlation(data):
    # Select relevant columns
    selected_columns = ['aqi', 'temperature_c', 'humidity_percent', 'wind_speed_ms']
    correlation_data = data[selected_columns]

    # Create the scatter matrix
    fig, ax = plt.subplots(figsize=(10, 10))  # Adjust figure size if needed
    scatter_axes = pd.plotting.scatter_matrix(
        correlation_data,
        alpha=0.5,
        figsize=(8, 8),  # Adjust the size of individual plots
        diagonal='kde',
        ax=None  # Leave this as None for matplotlib to handle
    )

    # Fix layout issues if any
    plt.suptitle("Correlation Between Weather Parameters and AQI")  # Add a title
    return plt.gcf()  # Return the figure object
