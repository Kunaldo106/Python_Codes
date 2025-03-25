import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_date_from_day_number(year, day_number):
    if not (1 <= day_number <= (366 if is_leap_year(year) else 365)):
        return "Invalid day number for the given year"

    date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=day_number - 1)
    return date.strftime("%A, %B %d, %Y")

# Example usage
year = 2006
day_number = 237
print(get_date_from_day_number(year, day_number))