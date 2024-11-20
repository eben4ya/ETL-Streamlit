import pandas as pd

def load_data():
    from dummy_data import generate_dummy_data
    return generate_dummy_data()

def filter_data(data, start_date, end_date):
    # Filter data by datetime_wib
    return data[(data['datetime_wib'] >= pd.Timestamp(start_date)) & (data['datetime_wib'] <= pd.Timestamp(end_date))]
