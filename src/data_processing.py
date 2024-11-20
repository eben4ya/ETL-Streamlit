import pandas as pd
import numpy as np
import pytz


def load_data():
    from dummy_data import generate_dummy_data
    return generate_dummy_data()


def filter_data(data, start_date, end_date):
    """
    Filter the data based on the specified date range (WIB).
    """
    # Convert start_date and end_date to pandas Timestamps
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    # Filter data based on 'Time of Record (WIB)'
    return data[(data['Time of Record (WIB)'] >= start_date) & (data['Time of Record (WIB)'] <= end_date)]


def calculate_regression_coefficients(data):
    # Define input variables (X) and output variable (Y)
    X = data[['temperature_c', 'humidity_percent',
              'pressure_hpa', 'wind_speed_ms']].values
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
