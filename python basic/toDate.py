from datetime import datetime

# Given year and month as integers
year = int(input('Enter a year: '))
month = int(input('Enter month (1-12):'))

# Create a date object (assuming the first day of the month)
date_obj = datetime(year, month, 1)

# Convert the date object to a string in the desired format
date_str = date_obj.strftime('%Y-%m-%d')

print(date_str)
print(date_obj.weekday())
