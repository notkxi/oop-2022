# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Apr 13, 2022
# Programming Homework: 05
#
# File: tripschedule.py

from date import Date
from trip import Trip


class TripSchedule:
    """This class is a container for Trip objects."""

    def __init__(self):
        """This constructor takes and stores a Trip object in a list."""

        # create empty list.
        self.__schedule = []

    def insert(self, trip):
        """This method takes one parameter trip, a trip object, and inserts it into
        the schedule list if the trip does not conflict with existing ones."""

        # loop through entire schedule.
        for trips in self.__schedule:

            # check if trip conflicts with trip already in the schedule list by using Trip
            # methods. If the trips overlaps or departure and arrival are the same as other
            # departure and arrivals then we raise an exception.
            if trip.departure() == trips.arrival():
                raise Exception("Departure is the same as the arrival of another trip.")
            if trip.arrival() == trips.departure():
                raise Exception("Arrival is the same as the departure of another trip.")
            if trip.overlaps(trips):
                raise Exception("Trip overlaps with another trip.")

        # add trip to schedule list.
        self.__schedule.append(trip)

    def delete(self, trip):
        """This method takes one parameter, trip, and removes the trip from the
        list schedule."""

        # use remove to remove trip from list.
        self.__schedule.remove(trip)

    def __len__(self):
        """Overload len function to return the total number of trips in the schedule."""

        # return amount of objects in list.
        return len(self.__schedule)

    def __getitem__(self, key):
        """Overloads index operator; takes key and returns the nth trip in the schedule."""

        # checks both positive and negative indexes
        # to ensure it does not go out of range.
        if key > len(self.__schedule) or key < -1 * (len(self.__schedule) + 1):
            raise IndexError("Index out of range.")

        # return element at the index.
        return self.__schedule[key]

    def __iter__(self):
        """Overload the iter operator to return an iterator of the schedule list."""

        # use the TripScheduleIterator to make and iterator object.
        return TripScheduleIterator(self.__schedule)

    def search(self, keyword):
        """This method takes one parameter, keyword, either a destination or a month,
        a string or integer, and returns all trips in the month or at the destination."""

        # make a copy of the schedule and sort it by the departure date.
        schedule_copy = sorted(self.__schedule, key=lambda x: x.departure())

        # create and empty list to store the key dates.
        keydates = []

        # if the input is an integer then loop though the schedule.
        if type(keyword) == int:
            for trip in schedule_copy:

                # use trip and date methods to return the
                # month and compare it to the keyword.
                if trip.departure().month() == keyword:

                    # append the results to the keydates list.
                    keydates.append(trip)

        # if it is a string then use trip methods to
        # compare it to the keyword.
        else:
            for trip in schedule_copy:

                # if equal to the keyword then append to list.
                if trip.destination() == keyword:
                    keydates.append(trip)

        # use for loop to print out the list.
        for trip in keydates:
            print(trip)

    def available(self, month, year):
        """This method takes two parameters, month and year, both integers, and
        searches the schedule for all available dates in the month of that year"""

        # create list of all the days in all the months, account for leap year.
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 100 != 0 and year % 4 == 0:
            monthdays[1] = 29

        # create list empty list to store used and unused dates.
        used_dates = []
        avaliable_dates = []

        # loop thought all trips in schedule.
        for trips in self.__schedule:

            # set a variable to the departure dates.
            date = trips.departure()

            # loop through all the used dates and add them to the used date list.
            for days in range(trips.duration() + 1):
                used_dates.append(date)
                date = date + 1

        # loop through all the days in the month.
        for i in range(1, monthdays[month + 1] + 1):

            # create date object to test every day in the month.
            dates = Date(month, i, year)

            # if the date is not in the used date list then
            # append it the available dates and return it.
            if dates not in used_dates:
                avaliable_dates.append(dates)
        return avaliable_dates

    def weekend_travel(self, yr):
        """This method takes one parameter yr, and integer, and searches the schedule for
        all trips in year that involve weekend travel. The function returns a list of all such trips."""

        # create copy of list and organize it by departure date.
        schedule_copy = sorted(self.__schedule, key=lambda x: x.departure())

        # create empty list to store the trips.
        trip_in_yr = []

        # loop through the organized list.
        for trips in schedule_copy:

            # if the trip is in the year then append to the
            # trip_in_yr list.
            if trips.departure().year() == yr:
                trip_in_yr.append(trips)

        # loop through the trip_in_yr list with enumerate
        # to delete the trip if need be.
        for count, trips in enumerate(trip_in_yr):

            # use trip method to see if the trip contains a weekend.
            # if it does not delete from the list.
            if not trips.containsweekend():
                del trip_in_yr[count]

        # return list.
        return trip_in_yr

    def earliest(self):
        """This method returns the trip in the schedule that has the earliest
        departure date of all the trips."""

        # create an organized list using sort function to sort all
        # trips in the schedule by their departure date.
        schedule_copy = sorted(self.__schedule, key=lambda x: x.departure())

        # return first entry.
        return schedule_copy[0]

    def last(self):
        """This method returns the trip in the schedule that has the latest
        departure date of all the trips."""

        # create an organized list using sort function to sort all
        # trips in the schedule by their departure date.
        schedule_copy = sorted(self.__schedule, key=lambda x: x.departure())

        # return last entry.
        return schedule_copy[-1]

    def sortbydeparture(self):
        """This method returns sorts all the trips in the schedule by their
        departure dates."""

        # use sort function to sort all trips in the schedule by their departure date.
        self.__schedule.sort(key=lambda x: x.departure())

    def __str__(self):
        """This returns a string representation of the trips."""
        return "\n".join([str(trip) for trip in self.__schedule])

    def __repr__(self):
        """This method also returns a string representation of the trips."""
        return str(self)

class TripScheduleIterator:
    """This class creates an iterator object for the trip schedule, it takes one
    parameter, triplist, a list."""

    def __init__(self, triplist):
        """This constructor store the list, the length of the list, and current position of the
        iterator."""

        self.list = triplist
        self.stop = len(self.list)
        self.current = 0

    def __next__(self):
        """Overloads next operator."""

        # if the index goes out of range return error.
        if self.current >= self.stop:
            raise StopIteration

        # else save whatever element is the at the self.current position in the list.
        current_trip = self.list[self.current]

        # add one to current to get next element.
        self.current += 1

        # return the current trip
        return current_trip
