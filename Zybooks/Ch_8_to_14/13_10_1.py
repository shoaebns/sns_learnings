from datetime import date, timedelta

# 1. Complete read_date()
def read_date():
    """Read a string representing a date in the format yyyy-mm-dd, create a
    date object from the input string, and return the date object
    """
    date_str = input()
    # Create a date object from the input string
    date_obj = date.fromisoformat(date_str)
    return date_obj

# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list
date_list = []
while len(date_list) < 4:
    date = read_date()
    date_list.append(date)

# 3. Use sorted() to sort the dates, earliest first
sorted_dates = sorted(date_list)

# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yyyy
for date in sorted_dates:
    formatted_date = date.strftime('%m/%d/%Y')
    print(formatted_date)

# 5. Output the number of days between the last two dates as a positive number
days_between = (sorted_dates[-1] - sorted_dates[-2]).days
print(days_between)

# 6. Output the date that is 3 weeks from the most recent date in the list
most_recent_date = sorted_dates[-1]
three_weeks_later = most_recent_date + timedelta(weeks=3)
formatted_future_date = three_weeks_later.strftime('%B %d, %Y')
print(formatted_future_date)

# 7. Output the full name of the day of the week of the earliest day
earliest_day_of_week = sorted_dates[0].strftime('%A')
print(earliest_day_of_week)
