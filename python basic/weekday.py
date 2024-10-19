from datetime import datetime

date_input = input("Enter a date (YYYY-MM-DD): ")

# Convert the input string to a datetime object
date_object = datetime.strptime(date_input, "%Y-%m-%d")

# Get the weekday (0=Monday, 6=Sunday)
weekday_number = date_object.weekday()

# List of weekday names
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the name of the weekday
print("The day of the week is:", weekdays[weekday_number])