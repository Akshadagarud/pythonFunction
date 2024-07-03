import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def calculate_time_intervals(start_date, end_date, interval_type):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    intervals = []

    if interval_type == 'monthly':
        current_date = start_date
        while current_date <= end_date:
            next_month = current_date + relativedelta(months=1)
            if next_month > end_date:
                if current_date.month != end_date.month or current_date.year != end_date.year:
                    intervals.append((current_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
                break
            else:
                intervals.append((current_date.strftime('%Y-%m-%d'), (next_month - timedelta(days=1)).strftime('%Y-%m-%d')))
            current_date = next_month
           
    
    elif interval_type == 'quarterly':
        current_date = start_date
        while current_date <= end_date:
           next_quarter = current_date + relativedelta(months=3)
           if next_quarter > end_date:
                if (current_date.month - 1) // 3 != (end_date.month - 1) // 3 or current_date.year != end_date.year:
                    intervals.append((current_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
                break
           else:
            intervals.append((current_date.strftime('%Y-%m-%d'), (next_quarter - timedelta(days=1)).strftime('%Y-%m-%d')))
            current_date = next_quarter

    
    elif interval_type == 'half_yearly':
        current_date = start_date
        while current_date <= end_date:
            next_half_year = current_date + relativedelta(months=6)
            if next_half_year > end_date:
                if (current_date.month - 1) // 6 != (end_date.month - 1) // 6 or current_date.year != end_date.year:
                    intervals.append((current_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
                break
            else:
                intervals.append((current_date.strftime('%Y-%m-%d'), (next_half_year - timedelta(days=1)).strftime('%Y-%m-%d')))
            current_date = next_half_year


    elif interval_type == 'yearly':
        current_date = start_date
        while current_date <= end_date:
            next_year = current_date + relativedelta(years=1)
            if next_year > end_date:
                if current_date.year != end_date.year:
                    intervals.append((current_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
                break
            else:
                intervals.append((current_date.strftime('%Y-%m-%d'), (next_year - timedelta(days=1)).strftime('%Y-%m-%d')))
            current_date = next_year

    return intervals

st.title("Date Calculator [Monthly Quaterly Half-Yearly Yearly]")

start_date = None
end_date = None
interval_type =None

start_date = st.date_input("Start date",start_date)
end_date = st.date_input("End date",end_date)
interval_type = st.selectbox("Select interval type", ['monthly', 'quarterly', 'half_yearly', 'yearly'],interval_type)

if st.button("Calculate Intreval"):
    if start_date > end_date:
        st.warning("Start date cannot be greater than end date. Enter a valid date range.")
    else:
        intervals = calculate_time_intervals(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), interval_type)
        if not intervals:
            st.write("Intervals not found in given range")
        else:
        st.write(f"Intervals of {interval_type} type:")
        for interval in intervals:
            st.write(f"From {"Start date: {interval[0]}  End date: {interval[1]}")
