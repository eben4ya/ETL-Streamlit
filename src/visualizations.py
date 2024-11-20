import matplotlib.pyplot as plt
import pandas as pd

def plot_aqi_trend(data):
    fig, ax = plt.subplots()
    data.groupby(data['datetime_wib'].dt.date)['aqi'].mean().plot(ax=ax)
    ax.set_title("AQI Trend Over Time (WIB)")
    ax.set_xlabel("Date (WIB)")
    ax.set_ylabel("Average AQI")
    return fig

def plot_aqi_distribution_by_weather_desc(data):
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size
    data.boxplot(column='aqi', by='weather_desc', ax=ax, grid=False, rot=45)
    ax.set_title("AQI Distribution by Weather Description")
    ax.set_xlabel("Weather Description")
    ax.set_ylabel("AQI")
    plt.suptitle("")  # Remove the default title added by pandas boxplot
    return fig


def plot_main_pollutant_by_weather_desc(data):
    # Group data by 'weather_desc' and count occurrences of 'main_pollutant'
    pollutant_counts = data.groupby('weather_desc')['main_pollutant'].value_counts().unstack()

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size
    pollutant_counts.plot(kind='bar', stacked=True, ax=ax)

    # Set titles and labels
    ax.set_title("Main Pollutants by Weather Description")
    ax.set_xlabel("Weather Description")
    ax.set_ylabel("Count")
    ax.legend(title="Main Pollutant", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # Adjust layout for better readability

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
