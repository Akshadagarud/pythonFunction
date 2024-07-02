import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calculate_intervals(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    intervals = {
        'monthly': [],
        'quarterly': [],
        'half_yearly': [],
        'yearly': []
    }

    # Calculate monthly intervals
    current_date = start_date
    while current_date < end_date:
        next_date = current_date + relativedelta(months=1)
        if next_date > end_date:
            next_date = end_date
        intervals['monthly'].append((current_date, next_date - timedelta(days=1)))
        current_date = next_date

    # Calculate quarterly intervals
    current_date = start_date
    while current_date < end_date:
        next_date = current_date + relativedelta(months=3)
        if next_date > end_date:
            next_date = end_date
        intervals['quarterly'].append((current_date, next_date - timedelta(days=1)))
        current_date = next_date

    # Calculate half-yearly intervals
    current_date = start_date
    while current_date < end_date:
        next_date = current_date + relativedelta(months=6)
        if next_date > end_date:
            next_date = end_date
        intervals['half_yearly'].append((current_date, next_date - timedelta(days=1)))
        current_date = next_date

    # Calculate yearly intervals
    current_date = start_date
    while current_date < end_date:
        next_date = current_date + relativedelta(years=1)
        if next_date > end_date:
            next_date = end_date
        intervals['yearly'].append((current_date, next_date - timedelta(days=1)))
        current_date = next_date

    return intervals

def main():
    st.title("Time Interval Calculator")
    st.write("Calculate monthly, quarterly, half-yearly, and yearly intervals.")

    # Set default start and end dates
    start_date = "2024-01-01"
    end_date = "2024-03-01"

    st.write(f"Start Date: {start_date}")
    st.write(f"End Date: {end_date}")

    if st.button("Calculate Intervals"):
        intervals = calculate_intervals(start_date, end_date)
        
        for key, value in intervals.items():
            st.write(f"{key.capitalize()} intervals:")
            if value:
                for interval in value:
                    st.write(f"Start: {interval[0].strftime('%Y-%m-%d')}, End: {interval[1].strftime('%Y-%m-%d')}")
            else:
                st.write("No data")
            st.write()

if __name__ == "__main__":
    main()
