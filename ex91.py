'''
Gregorian Date to Ordinal Date

An ordinal date consists of a year and a day within it, both of which are integers. The
year can be any year in the Gregorian calendar while the day within the year ranges
from one, which represents January 1, through to 365 (or 366 if the year is a leap
year) which represents December 31. Ordinal dates are convenient when computing
differences between dates that are a specific number of days (rather than months). For
example, ordinal dates can be used to easily determine whether a customer is within
a 90 day return period, the sell-by date for a food-product based on its production
date, and the due date for a baby.

Write a function named ordinalDate that takes three integers as parameters.
These parameters will be a day, month and year respectively. The function should
return the day within the year for that date as its only result. Create a main program
that reads a day, month and year from the user and displays the day within the year for
that date. Your main program should only run when your file has not been imported
into another program.

'''

def main():

    days_in_month = {
        '1': 31,
        '2': 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    while True:
        try:
            year = int(input("Enter the year: "))
        except ValueError:
            continue
        else:
            break
    
    leap_year = leapyear(year)
    
    while True:
        try:
            month = int(input("Enter the month (number 1-12): "))
            if month > 12:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    
    while True:
        try:
            day = int(input("Enter the day (number): "))
            if not leap_year and month == 2 and day > 28:
                raise ValueError
            if month != 2 and day > days_in_month[str(month)]:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    
    od = ordinaldate(day, month, year)
    print(f'{od} day of the year')

def leapyear(year):
    if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
    else:
        return False

def ordinaldate(day, month, year):
    
    days_dict = {
        '1': 31,
        '2': 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    days = 0
    for i in range(1, month):
        days = days + days_dict[str(i)]
    
    if month > 2 and leapyear(year):
        return days + day + 1
    else:
        return days + day
    

if __name__ == "__main__":
    main()