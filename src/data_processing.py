import pandas as pd
import numpy as np


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
    """
    Calculate regression coefficients for predicting AQI based on weather parameters.
    Input features: Temperature, Humidity, Pressure, Wind Speed.
    Target: AQI (CN).
    """
    # Extract input features (X) and target variable (Y)
    X = data[['Temperature (°C)', 'Humidity (%)',
              'Pressure', 'Wind Speed (m/s)']].values
    Y = data['AQI (CN)'].values

    # Add a bias term (intercept) to the input features
    X = np.c_[np.ones(X.shape[0]), X]

    # Compute regression coefficients using the normal equation
    coefficients = np.linalg.inv(X.T @ X) @ X.T @ Y
    return coefficients


def predict_aqi(coefficients, input_data):
    """
    Predict AQI based on the regression coefficients and input weather parameters.
    """
    # Add a bias term (intercept) to input data
    input_data = np.c_[np.ones(input_data.shape[0]), input_data]

    # Compute predictions
    predictions = input_data @ coefficients
    return predictions
