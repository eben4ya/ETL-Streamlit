import pandas as pd
import numpy as np
import pytz

def load_data():
    from dummy_data import generate_dummy_data
    return generate_dummy_data()

def filter_data(data, start_date, end_date):
    # Convert start_date and end_date to timezone-aware timestamps in Asia/Jakarta timezone
    jakarta_tz = pytz.timezone("Asia/Jakarta")
    start_date = pd.Timestamp(start_date).tz_localize(jakarta_tz)
    end_date = pd.Timestamp(end_date).tz_localize(jakarta_tz)
    
    # Filter the data using the timezone-aware timestamps
    return data[(data['datetime_wib'] >= start_date) & (data['datetime_wib'] <= end_date)]

def calculate_regression_coefficients(data):
    # Define input variables (X) and output variable (Y)
    X = data[['temperature_c', 'humidity_percent', 'pressure_hpa', 'wind_speed_ms']].values
    Y = data['aqi'].values

    # Add a bias term (intercept)
    X = np.c_[np.ones(X.shape[0]), X]

    # Calculate regression coefficients using the normal equation
    coefficients = np.linalg.inv(X.T @ X) @ X.T @ Y
    return coefficients

def predict_aqi(coefficients, input_data):
    # Add a bias term (intercept) to input data
    input_data = np.c_[np.ones(input_data.shape[0]), input_data]
    predictions = input_data @ coefficients
    return predictions
