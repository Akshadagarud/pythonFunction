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
    if (end_date - start_date).days >= 6 * 30:  # Approximately 6 months
        while current_date < end_date:
            next_date = current_date + relativedelta(months=6)
            if next_date > end_date:
                next_date = end_date
            intervals['half_yearly'].append((current_date, next_date - timedelta(days=1)))
            current_date = next_date
    else:
        intervals['half_yearly'] = []

    # Calculate yearly intervals
    current_date = start_date
    if (end_date - start_date).days >= 365:
        while current_date < end_date:
            next_date = current_date + relativedelta(years=1)
            if next_date > end_date:
                next_date = end_date
            intervals['yearly'].append((current_date, next_date - timedelta(days=1)))
            current_date = next_date
    else:
        intervals['yearly'] = []

    return intervals

def main():
    st.title("Time Interval Calculator")
    st.write("Calculate monthly, quarterly, half-yearly, and yearly intervals.")

    start_date = st.date_input("Start Date", value=None)
    end_date = st.date_input("End Date", value=None)

    if start_date and end_date:
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        st.write(f"Start Date: {start_date_str}")
        st.write(f"End Date: {end_date_str}")

        if st.button("Calculate Intervals"):
            intervals = calculate_intervals(start_date_str, end_date_str)
            
            for key, value in intervals.items():
                st.write(f"{key.capitalize()} intervals:")
                if value:
                    for interval in value:
                        st.write(f"Start: {interval[0].strftime('%Y-%m-%d')}, End: {interval[1].strftime('%Y-%m-%d')}")
                else:
                    st.write("No data")
                st.write()
    else:
        st.write("Please select both start and end dates.")


if __name__ == "__main__":
    main()
