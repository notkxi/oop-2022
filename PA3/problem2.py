# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Mar 7, 2022
# Programming Homework: 03
#
# File: problem2.py

class Date:
    """This class is used to hold Data objects information."""

    # Constants that hold the minimum year allowed, and the day
    # of the week on January 1st of the minimum year.
    min_year = 1800
    dow_jan1 = "Wednesday"

    def __init__(self, month, day, year):
        """This constructor take three parameters month, day, and year, and writes it to a
        value. This constructor also checks the validity of the month, day, and year. If the
        values do not fall into the correct value of the date, an exception will be raised."""

        # Default values.
        self.valid_month = 1
        self.valid_day = 1
        self.valid_year = Date.min_year

        # Checks the validity of the year and the month.
        if Date.min_year <= year:
            if 1 <= month <= 12:

                # Checks if the month goes over 31 day limit. If it does not
                # write values. If it does raise an exception to inform user.
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= day <= 31:
                        self.valid_month = month
                        self.valid_day = day
                        self.valid_year = year
                    else:
                        raise Exception("Day must be between 1 and 31 for the specified month")

                # Checks if the month goes over 30 day limit. If it does not
                # write values. If it does raise an exception to inform user.
                if month in [4, 6, 9, 11]:
                    if 1 <= day <= 30:
                        self.valid_month = month
                        self.valid_day = day
                        self.valid_year = year
                    else:
                        raise Exception("Day must be between 1 and 30 for the specified month")

                # Check if month is February, and determine if
                # the year is a leap year using year_is_leap method.
                if month == 2:
                    self.valid_year = year

                    # If it is not a leap year then the day should fall between
                    # 1 and 28. If it does write values. If not raise an exception to inform user.
                    if not self.year_is_leap():
                        if 1 <= day <= 28:
                            self.valid_month = month
                            self.valid_day = day
                        else:
                            self.valid_year = Date.min_year
                            raise Exception("Day must be between 1 and 28 for the specified month")

                    # If it is a leap year then the day should fall between
                    # 1 and 29. If it does write values. If not raise an exception to inform user.
                    if self.year_is_leap():
                        if 1 <= day <= 29:
                            self.valid_month = month
                            self.valid_day = day
                        else:
                            self.valid_year = Date.min_year
                            raise Exception("Day must be between 1 and 29 for the specified month and year")

            # Raise exception if month or year values are not valid.
            else:
                raise Exception("Month must be between 1 and 12")
        else:
            raise Exception(f"Year must greater or equal to {Date.min_year}")

    def month(self):
        """This function has no parameters and returns the month value."""
        return self.valid_month

    def day(self):
        """This function has no parameters and returns the day value."""
        return self.valid_day

    def year(self):
        """This function has no parameters and returns the year value."""
        return self.valid_year

    def year_is_leap(self):
        """This function takes no parameters and returns True if the year is a leap year,
        and False if it is not."""

        # Use leap rules to determine if the year is a leap year, return True if it is.
        # To be a leap year the number must be divisible by 4, however it is
        # an end-of-century year, it must be divisible by 400.
        if self.valid_year % 4 == 0 and (self.valid_year % 100 != 0 or self.valid_year % 400 == 0):
            return True
        else:
            return False

    def daycount(self):
        """This function takes no parameters and counts the amount of days between the
        two dates."""

        # List to hold how many days each month hold.
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Determine how many years are between the two dates.
        year_diff = self.valid_year - Date.min_year

        # Determine how many leap years are between the two dates.
        # For the leap years that are divisible by 400 add .5 to
        # get proper rounding.
        number_leap_years = year_diff//4 - year_diff//100 + int(year_diff / 400 + .5)

        # Transfer the amount of years to days.
        days_before_year = (year_diff * 365)

        # Calculate the amount of days using the previous defined variables.
        days = days_before_year + sum(days_in_month[:self.valid_month]) + self.valid_day + number_leap_years

        # Determine if the year is a leap year and if the month
        # is January or February. If it is remove a day.
        if self.year_is_leap() and self.valid_month <= 2:
            days -= 1
        return days

    def day_of_week(self):
        """This function takes no parameters and returns the day of the week
        of the date."""

        # Create a list of the days in a specific order
        # so that the index out does not go of range.
        days_of_the_week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday',
                            'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Find the index of the start day.
        start_day = days_of_the_week.index(Date.dow_jan1)

        # Add six and find take the remainder divided by 7 to determine
        # what day of the week it is. Return that day of the week from the list.
        if (self.daycount() + 6) % 7 == 0:
            return Date.dow_jan1
        if (self.daycount() + 6) % 7 == 1:
            return days_of_the_week[start_day + 1]
        if (self.daycount() + 6) % 7 == 2:
            return days_of_the_week[start_day + 2]
        if (self.daycount() + 6) % 7 == 3:
            return days_of_the_week[start_day + 3]
        if (self.daycount() + 6) % 7 == 4:
            return days_of_the_week[start_day + 4]
        if (self.daycount() + 6) % 7 == 5:
            return days_of_the_week[start_day + 5]
        if (self.daycount() + 6) % 7 == 6:
            return days_of_the_week[start_day + 6]

    def __str__(self):
        """This method returns a printable representation of the date."""

        # Create a list of months.
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

        # Return string with month.
        return f"{months[self.valid_month - 1]} {self.valid_day}, {self.valid_year}"

    def __repr__(self):
        """This method also returns a string representation of the date."""
        return str(self)


