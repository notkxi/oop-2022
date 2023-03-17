# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Mar 26, 2022
# Programming Homework: 04
#
# File: datefuns.py

# Import Date class.
from date import Date

# List of days in the months.
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# List of the days of the months.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


def weekend_dates(m, y):
    """This function takes two parameters, m, an integer, and y, also an integer.
    It prints all the weekend dates that occurs in the month m of year y."""

    # Create date object to test if it is a leap year.
    test_date = Date(m, 1, y)

    # If it is a leap year then change the days in February to 29.
    if test_date.year_is_leap():
        days_in_month[2] = 29

    # Create a for loop to loop through all the dates in the month.
    for i in range(1, days_in_month[m] + 1):

        # Create a date object to test all possible dates.
        dates = Date(m, i, y)

        # If the day_of_week method returns Saturday or Sunday for the specific date
        # then print out the date with what day of the week it is.
        if dates.day_of_week() == "Saturday" or dates.day_of_week() == "Sunday":
            print(f"{months[m - 1]} {i}, {y} ({dates.day_of_week()})")


def first_mondays(y):
    """This function takes one parameter, y, an integer, and
    prints the dates of the first Monday of every month in that year."""

    # Create a for loop to iterate through all the months in year.
    for m in range(1, 13):

        # Create a for loop to iterate through all the days in the specific month.
        for d in range(1, days_in_month[m] + 1):

            # Create a date object to test all possible dates.
            dates = Date(m, d, y)

            # If the day_of_week method returns monday, and the day is less that or equal to 7
            # (the first monday has to occur with 7 days of the month) then print the date.
            if dates.day_of_week() == "Monday" and d <= 7:
                print(dates)


def interval_schedule(start_date, end_date, interval):
    """This function takes three parameters, start_date, a Date object, end_date, a Date object, and interval, a
    positive integer. It returns a list of dates that occur every interval day, starting on start_date, and ending on
    , end_date."""

    # Create a list containing the start date.
    date_list = [start_date]

    # While the amount of days in end_date is greater than the last date plus the interval then
    # Add another date to the list.
    while end_date.daycount() >= date_list[-1].daycount() + interval:
        date_list.append(date_list[-1] + interval)

    # Return the list.
    return date_list



