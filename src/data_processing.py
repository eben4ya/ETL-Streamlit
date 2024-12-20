import pandas as pd
import numpy as np


def load_data():
    from dummy_data import generate_dummy_data
    return generate_dummy_data()


def filter_data(data, start_date, end_date):
    """
    Filter the data based on the specified date range (WIB).
    Handles cases where the 'Time of Record (WIB)' is a string or datetime.
    """
    # Ensure start_date and end_date are pandas Timestamps
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    # Ensure 'Time of Record (WIB)' is a datetime column
    if not pd.api.types.is_datetime64_any_dtype(data['Time of Record (WIB)']):
        data['Time of Record (WIB)'] = pd.to_datetime(data['Time of Record (WIB)'])

    # Filter data based on 'Time of Record (WIB)'
    filtered_data = data[(data['Time of Record (WIB)'] >= start_date) & (data['Time of Record (WIB)'] <= end_date)]

    return filtered_data


def calculate_regression_coefficients(data, alpha=0.1):
    """
    Calculate regression coefficients for predicting AQI using Ridge Regression (L2 Regularization).
    Input features: Temperature, Humidity, Pressure, Wind Speed.
    Target: AQI (CN).
    """
    # Extract input features (X) and target variable (Y)
    X = data[['Temperature (°C)', 'Humidity (%)',
              'Pressure', 'Wind Speed (m/s)']].values
    Y = data['AQI (CN)'].values

    # Add a bias term (intercept) to the input features
    X = np.c_[np.ones(X.shape[0]), X]

    # Compute Ridge Regression coefficients
    # Ridge Regression formula: (X^T X + alpha*I)^-1 X^T Y
    n_features = X.shape[1]
    identity = np.eye(n_features)  # Identity matrix
    identity[0, 0] = 0  # Do not regularize the bias term
    coefficients = np.linalg.inv(X.T @ X + alpha * identity) @ X.T @ Y

    return coefficients


def predict_aqi(coefficients, input_data, noise_std=5):
    """
    Predict AQI based on the regression coefficients and input weather parameters.
    Add variability to predictions using random noise.
    """
    # Add a bias term (intercept) to input data
    input_data = np.c_[np.ones(input_data.shape[0]), input_data]

    # Compute predictions
    predictions = input_data @ coefficients

    # Add random noise to predictions for variability
    noise = np.random.normal(0, noise_std, size=predictions.shape)
    predictions += noise

    return predictions

