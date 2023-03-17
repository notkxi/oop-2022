# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: May 2, 2022
# Programming Homework: 06
#
# File: polys.py

# import math to use methods.
import math


class Point:
    """This class is used to hold Point objects information and methods."""

    def __init__(self, x = 0, y = 0):
        """This constructor takes two parameter x, an integer
        or float, and y, an integer or float, and stores it."""

        self.__x = x
        self.__y = y

    def translate(self, s, t):
        """This method takes two parameters, s, an integer or float, and t, an
        integer or float, and adds it to self.x and self.y respectively."""

        self.__x += s
        self.__y += t

    def rotate(self, degree):
        """This method takes one parameter, degree, an integer or float, and rotates
         the point around the point (0,0) by the degree."""

        # convert the degree measure to radians.
        rad = math.radians(degree)

        # use math functions and formulas to calculate
        # the rotated points and save it in self.x and self.y.
        x = self.__x * math.cos(rad) - self.__y * math.sin(rad)
        y = self.__x * math.sin(rad) + self.__y * math.cos(rad)
        self.__x = x
        self.__y = y

    def distance(self, p):
        """This method takes one parameter, p, a point, and finds
        the distance between the points self and p."""

        # use math functions and distance formula to calculate
        # the distance between the two points. Return the distance.
        distance = math.sqrt(((self.__x - p.__x) ** 2) + ((self.__y - p.__y) ** 2))
        return distance

    def left_of(self, q, r):
        """This method takes two parameters, p and r, points, and returns True if self lies to the left of
        the segment qr."""

        # uses formula to check if the point lies to the left of the line qr.
        # Returns true if the formula is greater than zero.
        if ((r.__x * self.__y - self.__x * r.__y) + (q.__x * r.__y - q.__x * self.__y) + (q.__y * self.__x - q.__y * r.__x)) > 0:
            return True
        return False

    def right_of(self, q, r):
        """This method takes two parameters, p and r, points, and returns True if self lies to the right of
        the segment qr."""

        # uses formula to check if the point lies to the right of the line qr.
        # Returns true if the formula is greater less zero.
        if ((r.__x * self.__y - self.__x * r.__y) + (q.__x * r.__y - q.__x * self.__y) + (q.__y * self.__x - q.__y * r.__x)) < 0:
            return True
        return False

    def __str__(self):
        """This method returns a printable representation of the point."""
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        """This method also returns a string."""
        return str(self)


class SimplePoly:
    """This class is used to hold SimplePoly objects information and methods."""

    def __init__(self, *vertices):
        """This constructor stores an arbitrary amount of
        points that form a polygon."""

        self.__points = list(vertices)

    def translate(self, s, t):
        """This method takes two parameters, s, an integer or float, and t, an
        integer or float, and adds it to every point in the list self.points."""

        # using for loop to translate every point by s and t.
        for point in self.__points:
            point.translate(s, t)

    def rotate(self, degree):
        """This method takes one parameter, degree, an integer or float, and rotates
        every point in self.points around the point (0,0) by the degree."""

        # using for loop to rotate every point in self.points by the degree.
        for point in self.__points:
            point.rotate(degree)

    def __iter__(self):
        """Overload the iter operator to return an iterator of the point list."""

        # use the SimplePolyIterator to make and iterator object.
        return SimplePolyIterator(self.__points)

    def __len__(self):
        """Overload len function to return the total number of points."""

        # return amount of objects in list.
        return len(self.__points)

    def __getitem__(self, key):
        """Overloads index operator; takes key and returns the nth trip in the schedule."""

        # raise error is key is larger than the amount of items
        # in the list, and if it is below zero.
        if key > len(self.__points) or key < 0:
            raise IndexError("Index out of range.")

        # return element at the index.
        return self.__points[key]

    def __str__(self):
        """This returns a string representation of the points."""
        return "\n".join([str(point) for point in self.__points])

    def perimeter(self):
        """This method returns the perimeter of the polygon."""

        # set distance to 0.
        perimeter = 0

        # loop through the list leaving out the last point.
        for point in range(len(self.__points) - 1):

            # calculate the distance between the current point and the one next to it.
            perimeter += self.__points[point].distance(self.__points[point + 1])

        # calculate the distance between the first point and last point and add it to the distance.
        perimeter += self.__points[0].distance(self.__points[-1])

        # return the distance.
        return perimeter


class ConvPoly(SimplePoly):
    """This class checks the if the vertices form a convex polygon.
    If it is not raise an exception."""

    def __init__(self, *vertices):
        """This constructor stores an arbitrary amount of
        points that form a convex polygon."""

        super().__init__(*vertices)
        """Using super to inherit the SimplePoly class."""

        # creating a list of the points.
        self.__points = list(vertices)

        # create empty list to store the point violates the convex polygon rule.
        convex = []

        # loop thorough all the points in the list.
        for i in range(len(self.__points)):
            # this is the checking the last point.
            if i == (len(self.__points) - 1):
                # append the result of left_of to the list for the last point.
                convex.append(self.__points[-1].left_of(self.__points[0], self.__points[1]))
            # this is checking the second to last point.
            elif i == (len(self.__points) - 2):
                # append the result of left_of to the list second to last point.
                convex.append(self.__points[-2].left_of(self.__points[-1], self.__points[0]))
            # this is checking the rest of the points.
            else:
                # append the result of left_of to the list for the rest of the points.
                convex.append(self.__points[i].left_of(self.__points[i + 1], self.__points[i + 2]))

            # if False is in the list that meant there is a violation of the convex polygon rule.
            if False in convex:
                raise Exception("Not a Convex Polygon")


class EquiTriangle(ConvPoly):
    """This class is a subclass of ConvPoly. It stores instances of equilateral triangles."""

    def __init__(self, length):
        """This constructor takes a single parameter length, which is the three lengths
        of the triangle."""
        self.__length = length

        # customizing the ConvPoly constructor passing the three points of the equilateral triangle to form
        # the triangle. Use math functions and pythagorean theorem to find the points of the triangle.
        super().__init__(Point(0,0), Point(self.__length, 0),
                         Point(self.__length / 2, math.sqrt((self.__length ** 2) - (self.__length / 2) ** 2)))

    def area(self):
        """This method finds and returns the area of the equatorial triangle."""

        # return the area of the triangle.
        return (math.sqrt(3) / 4) * (self.__length ** 2)


class Rectangle(ConvPoly):
    """This class is a subclass of ConvPoly. It stores instances of rectangles."""

    def __init__(self, length, width):
        """This constructor takes two parameters length and width, numbers, it represents the length
        and width of the rectangle."""
        self.__length = length
        self.__width = width

        # customizing the ConvPoly constructor passing
        # through the four points of the rectangle.
        super().__init__(Point(0, 0), Point(self.__length, 0),
                         Point(self.__length, self.__width), Point(0, self.__width))

    def area(self):
        """This method finds and returns the area of the rectangle."""

        # Returns the length times the width.
        return self.__length * self.__width


class Square(Rectangle):
    """This class is a subclass of the class Rectangle. It stores instances of squares."""

    def __init__(self, length):
        """This constructor takes one parameter length, the length of the side of the
        square."""
        self.__length = length

        super().__init__(self.__length, self.__length)
        """This customizes the rectangle constructor and passes through the length, as the two distances, 
        as all sides of a square are equal."""


class SimplePolyIterator:
    """This class creates an iterator object for the point list."""

    def __init__(self, pointlist):
        """This constructor stores the list, the length of the list, and current position of the
        iterator."""

        self.__list = pointlist
        self.__stop = len(self.__list)
        self.__current = 0

    def __next__(self):
        """Overloads next operator."""

        # if the index goes out of range return error.
        if self.__current >= self.__stop:
            raise StopIteration

        # else save whatever element is the at the self.current position in the list.
        current_point = self.__list[self.__current]

        # add one to current to get next element.
        self.__current += 1

        # return the current trip.
        return current_point










