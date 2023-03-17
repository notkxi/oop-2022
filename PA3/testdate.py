"""
This is a test module for the Date class implementation in problem2.py
"""

from problem2 import Date

def test_Date_methods():

    print("------------------------------------------------------")
    print("Welcome to the Date class! (calendar Dates, that is :)")
    print("------------------------------------------------------\n")

    print("I will first test your implementation of the constructor and the __str__ method.")
    print("I have created some instances of the Date class, which are printed below:\n")

    firstdate = Date(1,1,Date.min_year)
    indday = Date(7, 4, 1876)
    xmas = Date(12, 25, 2018)
    millenium = Date(1, 1, 2000)
    leapday = Date(2, 29, 2016)

    print(firstdate)
    print(indday)
    print(xmas)
    print(millenium)
    print(leapday)

    print("\nTesting the .year_is_leap() method...")
    print("-------------------------------------\n")

    if firstdate.year_is_leap():
        print(firstdate.year(), "is a leap year. (INCORRECT ANSWER)")
    else: 
        print(firstdate.year(), "is not a leap year. (CORRECT ANSWER)")

    if indday.year_is_leap():
        print(indday.year(), "is a leap year. (CORRECT ANSWER)")
    else: 
        print(indday.year(), "is not a leap year. (INCORRECT ANSWER)")

    if xmas.year_is_leap():
        print(xmas.year(), "is a leap year. (INCORRECT ANSWER)")
    else: 
        print(xmas.year(), "is not a leap year. (CORRECT ANSWER)")

    if millenium.year_is_leap():
        print(millenium.year(), "is a leap year. (CORRECT ANSWER)")
    else: 
        print(millenium.year(), "is not a leap year. (INCORRECT ANSWER)")

    print("\nTesting the .daycount() method...")
    print("---------------------------------\n")

    print("daycount for ", firstdate, "is", firstdate.daycount(), " (CORRECT ANSWER: 1)")
    print("daycount for ", indday, "is", indday.daycount(), " (CORRECT ANSWER: 27944)")
    print("daycount for ", xmas, "is", xmas.daycount(), " (CORRECT ANSWER: 79982)")
    print("daycount for ", millenium, "is", millenium.daycount(), " (CORRECT ANSWER: 73049)")
    print("daycount for ", leapday, "is", leapday.daycount(), " (CORRECT ANSWER: 78952)")    
    
    print("\nTesting the .day_of_week() method...")
    print("------------------------------------\n")

    print(firstdate, " is a ", firstdate.day_of_week(), "(CORRECT ANSWER: Wednesday)")
    print(indday, " is a ", indday.day_of_week(), "(CORRECT ANSWER: Tuesday)")
    print(xmas, " is a ", xmas.day_of_week(), "(CORRECT ANSWER: Tuesday)")
    print(millenium, " is a ", millenium.day_of_week(), "(CORRECT ANSWER: Saturday)")
    print(leapday, " is a ", leapday.day_of_week(), "(CORRECT ANSWER: Monday)")

    print("\nAnd that's all, folks! Goodbye!\n")
    
if __name__ == "__main__":
    test_Date_methods()
    
