import pandas as pd
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
