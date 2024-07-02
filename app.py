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

    start_date = st.date_input("Start Date", datetime.now())
    end_date = st.date_input("End Date", datetime.now() + relativedelta(months=1))

    if st.button("Calculate Intervals"):
        intervals = calculate_intervals(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        
        for key, value in intervals.items():
            st.write(f"{key.capitalize()} intervals:")
            for interval in value:
                st.write(f"Start: {interval[0].strftime('%Y-%m-%d')}, End: {interval[1].strftime('%Y-%m-%d')}")
            st.write()

if __name__ == "__main__":
    main()
