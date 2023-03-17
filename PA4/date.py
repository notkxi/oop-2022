# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Mar 26, 2022
# Programming Homework: 04
#
# File: date.py

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
        self.__valid_month = 1
        self.__valid_day = 1
        self.__valid_year = Date.min_year

        # Checks the validity of the year and the month.
        if Date.min_year <= year:
            if 1 <= month <= 12:

                # Checks if the month goes over 31 day limit. If it does not
                # write values. If it does raise an exception to inform user.
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= day <= 31:
                        self.__valid_month = month
                        self.__valid_day = day
                        self.__valid_year = year
                    else:
                        raise Exception("Day must be between 1 and 31 for the specified month")

                # Checks if the month goes over 30 day limit. If it does not
                # write values. If it does raise an exception to inform user.
                if month in [4, 6, 9, 11]:
                    if 1 <= day <= 30:
                        self.__valid_month = month
                        self.__valid_day = day
                        self.__valid_year = year
                    else:
                        raise Exception("Day must be between 1 and 30 for the specified month")

                # Check if month is February, and determine if
                # the year is a leap year using year_is_leap method.
                if month == 2:
                    self.__valid_year = year

                    # If it is not a leap year then the day should fall between
                    # 1 and 28. If it does write values. If not raise an exception to inform user.
                    if not self.year_is_leap():
                        if 1 <= day <= 28:
                            self.__valid_month = month
                            self.__valid_day = day
                        else:
                            self.__valid_year = Date.min_year
                            raise Exception("Day must be between 1 and 28 for the specified month")

                    # If it is a leap year then the day should fall between
                    # 1 and 29. If it does write values. If not raise an exception to inform user.
                    if self.year_is_leap():
                        if 1 <= day <= 29:
                            self.__valid_month = month
                            self.__valid_day = day
                        else:
                            self.__valid_year = Date.min_year
                            raise Exception("Day must be between 1 and 29 for the specified month and year")

            # Raise exception if month or year values are not valid.
            else:
                raise Exception("Month must be between 1 and 12")
        else:
            raise Exception(f"Year must greater or equal to {Date.min_year}")

    def month(self):
        """This function has no parameters and returns the month value."""
        return self.__valid_month

    def day(self):
        """This function has no parameters and returns the day value."""
        return self.__valid_day

    def year(self):
        """This function has no parameters and returns the year value."""
        return self.__valid_year

    def year_is_leap(self):
        """This function takes no parameters and returns True if the year is a leap year,
        and False if it is not."""

        # Use leap rules to determine if the year is a leap year, return True if it is.
        # To be a leap year the number must be divisible by 4, however it is
        # an end-of-century year, it must be divisible by 400.
        if self.__valid_year % 4 == 0 and (self.__valid_year % 100 != 0 or self.__valid_year % 400 == 0):
            return True
        else:
            return False

    def daycount(self):
        """This function takes no parameters and counts the amount of days between the
        two dates."""

        # List to hold how many days each month hold.
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Determine how many years are between the two dates.
        year_diff = self.__valid_year - Date.min_year

        # Determine how many leap years are between the two dates.
        # For the leap years that are divisible by 400 add .5 to
        # get proper rounding.
        number_leap_years = year_diff//4 - year_diff//100 + int(year_diff / 400 + .5)

        # Transfer the amount of years to days.
        days_before_year = (year_diff * 365)

        # Calculate the amount of days using the previous defined variables.
        days = days_before_year + sum(days_in_month[:self.__valid_month]) + self.__valid_day + number_leap_years

        # Determine if the year is a leap year and if the month
        # is January or February. If it is remove a day.
        if self.year_is_leap() and self.__valid_month <= 2:
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

    def nextday(self):
        # List to hold how many days each month hold.
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If it is the last day in the year, return the first day of the next year.
        if self.__valid_month == 12 and self.__valid_day == 31:
            return Date(1, 1, self.__valid_year + 1)

        # If it is February, a leapyear, and it is a leap day then return March 1st
        # of the same year.
        elif self.__valid_month == 2 and self.year_is_leap():
            if self.__valid_day == 29:
                return Date(3, 1, self.__valid_year)
            # If it is not a leap day then add one day.
            else:
                return Date(self.__valid_month, self.__valid_day + 1, self.__valid_year)

        # If it is the last day of the month then return the first day of the next month.
        elif days_in_month[self.__valid_month] == self.__valid_day:
            return Date(self.__valid_month + 1, 1, self.__valid_year)

        # If else add one day.
        else:
            return Date(self.__valid_month, self.__valid_day + 1, self.__valid_year)

    def prevday(self):
        # List to hold how many days each month hold.
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If the date attempts to exceed the minimum year then raise an exception.
        if self.__valid_day == 1 and self.__valid_month == 1:
            if self.__valid_year == Date.min_year:
                raise Exception("Exceeds minimum year.")
            # If else return the last day of the prior year.
            else:
                return Date(12, 31, self.__valid_year - 1)

        # If it is the first day of a month then return the prior month, with whatever
        # the last day of the prior month is.
        if self.__valid_day == 1:
            # However, it is March and a leap year, then return leap day.
            if self.__valid_month == 3 and self.year_is_leap():
                return Date(2, 29, self.__valid_year)
            else:
                return Date(self.__valid_month - 1, days_in_month[self.__valid_month - 1], self.__valid_year)
        # If else subtract one day.
        else:
            return Date(self.__valid_month, self.__valid_day - 1, self.__valid_year)

    def __str__(self):
        """This method returns a printable representation of the date."""

        # Create a list of months.
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

        # Return string with month.
        return f"{months[self.__valid_month - 1]} {self.__valid_day}, {self.__valid_year}"

    def __repr__(self):
        """This method also returns a string representation of the date."""
        return str(self)

    def __add__(self, n):
        """This method overloads the + operator. It contains two parameters: self and an integer
         n. It returns the date the occurs n days after the date self."""

        # Create a date object.
        date = Date(self.__valid_month, self.__valid_day, self.__valid_year)

        # Use the next day method to add one day for the amount of days n contains.
        for i in range(n):
            date = date.nextday()

        # Return date object.
        return date

    def __sub__(self, n):
        """This method overloads the - operator. It contains two parameters: self and an integer
        n. It returns the date the occurs n days before the date self."""

        # Create a date object.
        date = Date(self.__valid_month, self.__valid_day, self.__valid_year)

        # Use the prev day method to subtract one day for the amount of days n contains.
        for i in range(n):
            date = date.prevday()

        # Return date object.
        return date

    def __lt__(self, other):
        """This method overloads the < operator. It has two parameters: self and other,
        which is a date. It returns True if self comes before other."""
        return self.daycount() < other.daycount()

    def __eq__(self, other):
        """This method overloads the == operator. It has two parameters: self and other,
        which is a date. It returns True if self is equal to other."""
        return self.daycount() == other.daycount()

    def __le__(self, other):
        """This method overloads the <= operator. It has two parameters: self and other,
        which is a date. It returns True if self is less than or equal to other."""
        return self.daycount() <= other.daycount()

    def __gt__(self, other):
        """This method overloads the > operator. It has two parameters: self and other,
        which is a date. It returns True if self is greater than other."""
        return self.daycount() > other.daycount()

    def __ge__(self, other):
        """This method overloads the >= operator. It has two parameters: self and other,
        which is a date. It returns True if self is greater or equal to than other."""
        return self.daycount() >= other.daycount()

    def __ne__(self, other):
        """This method overloads the != operator. It has two parameters: self and other,
        which is a date. It returns True if self is not equal to other."""
        return self.daycount() != other.daycount()


