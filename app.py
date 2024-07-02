import streamlit as st
from datetime import datetime, timedelta

def calculate_time_intervals(start_date, end_date, interval_type):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    intervals = []

    if interval_type == 'monthly':
        current_date = start_date
        while current_date <= end_date:
            next_month = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
            intervals.append((current_date.strftime('%Y-%m-%d'), (next_month - timedelta(days=1)).strftime('%Y-%m-%d')))
            current_date = next_month

    elif interval_type == 'quarterly':
        current_date = start_date
        while current_date <= end_date:
            intervals.append((current_date.strftime('%Y-%m-%d'), (current_date + timedelta(days=90)).strftime('%Y-%m-%d')))
            current_date = current_date + timedelta(days=90)

    elif interval_type == 'half_yearly':
        current_date = start_date
        while current_date <= end_date:
            intervals.append((current_date.strftime('%Y-%m-%d'), (current_date + timedelta(days=180)).strftime('%Y-%m-%d')))
            current_date = current_date + timedelta(days=180)

    elif interval_type == 'yearly':
        current_date = start_date
        while current_date <= end_date:
            intervals.append((current_date.strftime('%Y-%m-%d'), (current_date + timedelta(days=365)).strftime('%Y-%m-%d')))
            current_date = current_date + timedelta(days=365)

    return intervals

st.title("Date Calculator [Monthly Quaterly Half-Yearly Yearly]")

start_date = None
end_date = None
interval_type =None

start_date = st.date_input("Start date")
end_date = st.date_input("End date")
interval_type = st.selectbox("Select interval type", ['monthly', 'quarterly', 'half_yearly', 'yearly'])

if st.button("Calculate Intreval"):
    if start_date > end_date:
        st.warning("Start date cannot be greater than end date. Enter a valid date range.")
    else:
        intervals = calculate_time_intervals(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), interval_type)
        st.write(f"Intervals of {interval_type} type:")
        for interval in intervals:
            st.write(f"From {interval[0]} to {interval[1]}")
