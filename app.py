import streamlit as st
from datetime import datetime
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

    current_date = start_date

    # Calculate monthly intervals
    while current_date <= end_date:
        next_month_end = min(current_date + relativedelta(months=1, day=1) - relativedelta(days=1), end_date)
        intervals['monthly'].append((current_date, next_month_end))
        current_date = next_month_end + relativedelta(days=1)

    current_date = start_date

    # Calculate quarterly intervals
    while current_date <= end_date:
        next_quarter_end = min(current_date + relativedelta(months=3, day=1) - relativedelta(days=1), end_date)
        intervals['quarterly'].append((current_date, next_quarter_end))
        current_date = next_quarter_end + relativedelta(days=1)

    current_date = start_date

    # Calculate half-yearly intervals
    while current_date <= end_date:
        next_half_year_end = min(current_date + relativedelta(months=6, day=1) - relativedelta(days=1), end_date)
        intervals['half_yearly'].append((current_date, next_half_year_end))
        current_date = next_half_year_end + relativedelta(days=1)

    # Calculate yearly intervals
    current_date = start_date
    while current_date <= end_date:
        next_year_end = min(current_date + relativedelta(years=1, day=1) - relativedelta(days=1), end_date)
        intervals['yearly'].append((current_date, next_year_end))
        current_date = next_year_end + relativedelta(days=1)

    return intervals

def main():
    st.title("Time Interval Calculator")
    st.write("Calculate monthly, quarterly, half-yearly, and yearly intervals.")

    start_date = st.date_input("Start Date", value=None)
    end_date = st.date_input("End Date", value=None)

    if start_date and end_date:
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        if st.button("Calculate Intervals"):
            intervals = calculate_intervals(start_date_str, end_date_str)
            
            st.write(f"Start Date: {start_date_str}")
            st.write(f"End Date: {end_date_str}")
            
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
