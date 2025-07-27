from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date
current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = display_current_datetime() + timedelta(days=number_of_days)
    return f"The future date is: {future_date.strftime('%Y-%m-%d')}"

print(calculate_future_date())
