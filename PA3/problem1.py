# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Mar 7, 2022
# Programming Homework: 03
#
# File: problem1.py

def replace_char(astr, old_char, new_char):
    """This function takes three parameters, astr, a string, old_char, a string, and new_char, a string.
        The function returns a string in which every occurrence of old char in astr is replaced with new char."""

    # The base case of this recursion method. If the string,
    # astr, contains zero characters return astr.
    if len(astr) == 0:
        return astr

    # If the first character of astr contains the old character return the
    # new character plus the rest of the string ran through the replace_char function.
    # We do this to replace every instance of the old character throughout the sting.
    if astr[0] == old_char:
        return new_char + replace_char(astr[1:], old_char, new_char)

    # If the current character does not contain the new character then
    # return the current character plus the rest of the string ran through
    # the replace_char function.
    else:
        return astr[0] + replace_char(astr[1:], old_char, new_char)


def occurrences(astr, substr):
    """This function takes two parameters astr, a string, and substr, another string.
        The function returns the number of times the substring substr appears in the string astr."""

    # Find the length of substr for later use.
    len_substr = len(substr)

    # The base case of this recursion method.
    # If the string, astr is empty return 0.
    if len(astr) == 0:
        return 0

    # If the len_substr is equal to substr then that means
    # that there is an instance of substr in the string. Add 1 to mark this down.
    if astr[:len_substr] == substr:
        return occurrences(astr[len_substr:], substr) + 1

    # If else there is not an instance of substr in the sting astr
    # Iterate next position in string to check remaining characters in string.
    else:
        return occurrences(astr[1:], substr)


def inverse_pair(L):
    """This function takes one parameter L, a list, and returns True if L
    contains a pair of integers whose sum is zero and False otherwise"""

    # The base case of this recursion method. If the list, has two integers
    # then return the result of the two integers added together equal to zero.
    if len(L) == 2:
        return L[0] + L[1] == 0

    # If L[0] + L[1] equals zero return true. Use [] to create a list to concatenate the two list together
    # to get every list combination. Also include L[1:] to not skip over any list elements.
    if L[0] + L[1] == 0 or inverse_pair([L[0]] + L[2:]) or inverse_pair(L[1:]):
        return True

    # If none of the prior conditions are met then return False.
    else:
        return False

