# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Mar 26, 2022
# Programming Homework: 04
#
# File: bagfunctions.py

# Import bag to use methods.
from bag import Bag


def remove_item(B, item):
    """This function takes two parameters B, a Bag object, and item, an item.
    It removes all occurrences of item from B."""

    # Take a count of how many times item occurs in the bag.
    count = B.count(item)

    # Create a for loop and the erase_one method, to erase the item for however
    # many times it occurs in the bag.
    for i in range(count):
        B.erase_one(item)


def remove_repeats(B):
    """This function takes a single parameter B, a bag object. It removes
    all repeating items in the bag, leaving one copy of each item in the bag."""

    # Create a list of all items in the bag.
    bag_list = B.items()

    # Iterate thought each object in the list.
    for i in bag_list:

        # While the count of the item in the bag is over 1 delete the item from the bag.
        while B.count(i) > 1:
            B.erase_one(i)


def mode(B):
    """This function takes one parameter B, a bag object. The function returns a
    list of the most frequently occurring items in the bag."""

    # Create a list of items in the bag.
    bag_list = B.items()

    # Create a variable that stores the highest amount of times an item in the bag occurs.
    most_common = B.count(max(bag_list, key=bag_list.count))

    # Return a list that returns a contains the highest occurring items.
    return [item for item in bag_list if B.count(item) == most_common]


def union(B1, B2):
    """This function takes two parameters, B1, a bag objects, B2, another bag object. It creates a union
     of the two bags, which is a bag that contains all the items from B1 and B2."""

    # Create an empty bag object.
    B3 = Bag()

    # Create a list of the items from both B1 ang B2.
    b3_lst = B1.items() + B2.items()

    # Create a for loop to iterate through all items in b3_list.
    for i in b3_lst:

        # Use a while loop so the amount of times that the item occurs in B1 and B2 is equal to B3.
        while b3_lst.count(i) != B1.count(i) + B2.count(i):
            b3_lst += [i]

        # Insert the item in to the bag B3.
        B3.insert(i)

    # Return B3.
    return B3


def intersection(B1, B2):
    """This function takes two parameters, B1, a bag objects, B2, another bag object. It creates an intersection
    of the two bags, which is a bag that contains all the items that are common to both B1 and B2."""

    # Create a empty bag object and list.
    B3 = Bag()
    b3_list = []

    # Create a lists of items in both bags.
    b1_list = B1.items()
    b2_list = B2.items()

    # Use for loops to iterate through all items in both lists. Use while loop so the amount of times
    # that the item occurs in the original bag is equal to the amount of times in occurs in the list.
    for i in b1_list:
        while b1_list.count(i) != B1.count(i):
            b1_list += [i]
    for i in b2_list:
        while b2_list.count(i) != B2.count(i):
            b2_list += [i]


    # Use for loop to iterate through all items in the first list.
    for x in b1_list:
        # If the items is in both b1 and b2 then append it to the b3 list and remove it from b2 list.
        if x in b2_list:
            b2_list.remove(x)
            b3_list.append(x)

    # Insert items in to the B3 bag.
    for i in b3_list:
        B3.insert(i)

    # Return B3.
    return B3