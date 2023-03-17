# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Feb 1, 2022
# Programming Homework: 01
#
# File: problem1.py


def multi_column_print(L, numcols):
    """A function with two arguments, L, a list, and numcols, an integer, that will print
    out the list according to how many columns the user inputs."""

    # Mapping every element in list L to a string, and converting back into a list.
    L = list(map(str, L))

    # Finding the longest string in the list L, and determining the length of it.
    longest_ele = len(max(L, key=len))

    # Creating a count variable to keep track of how many elements in the list L
    # are printed to the screen.
    count = 0

    # Create a for loop to iterate thorough every element in the list L.
    for i in L:

        # Determining how much whitespace is needed to correctly align all the columns.
        space = longest_ele - len(i)
        
        print(" " * space + i, end = " ")
        count = count + 1

        if count == (numcols):
            print()
            count = 0

multi_column_print([2**i for i in range(20)], 5)