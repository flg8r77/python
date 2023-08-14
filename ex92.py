'''
Ordinal date to Georgian Date

Create a function that takes an ordinal date, consisting of a year and a day within in
that year, as its parameters. The function will return the day and month correspond-
ing to that ordinal date as its results. Ensure that your function handles leap years
correctly.
    Use your function, as well as the ordinalDate function that you wrote previ-
ously, to create a program that reads a date from the user. Then your program should
report a second date that occurs some number of days later. For example, your pro-
gram could read the date a product was purchased and then report the last date that
it can be returned (based on a return period that is a particular number of days), or
your program could compute the due date for a baby based on a gestation period of
280 days. Ensure that your program correctly handles cases where the entered date
and the computed date occur in different years
'''

from ex91 import leapyear, georgian_to_ordinal, get_georgian_date

def main():

    return_period = 120
    georgian_day, georgian_month, georgian_year = get_georgian_date()
    ordinal_day, ordinal_year = georgian_to_ordinal(georgian_day, georgian_month, georgian_year)
    ordinal_day = ordinal_day + return_period
    while True:
        if leapyear(ordinal_year) and ordinal_day > 366:
            ordinal_day = ordinal_day - 366
            ordinal_year += 1
        elif not leapyear(ordinal_year) and ordinal_day > 365:
            ordinal_day = ordinal_day - 365
            ordinal_year += 1
        else:
            break
    final_day, final_month, final_year = ordinal_to_georgian(ordinal_year, ordinal_day)
    print(f'Return ({return_period} days) valid until {final_day} {final_month}, {final_year}')
         

def get_ordinal_date():
    while True:
        try:
            year = int(input("Enter the Ordinal year: "))
        except ValueError:
            continue
        else:
            break
    
    while True:
        try:
            day = int(input("Enter the Ordinal day: "))
            if not leapyear(year) and day > 365:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    return day, year

def ordinal_to_georgian(year, day):
    days_in_month = {
        1: {'month': 'January', 'days': 31},
        2: {'month': 'Feburary', 'days': 28},
        3: {'month': 'March', 'days': 31},
        4: {'month': 'April', 'days': 30},
        5: {'month': 'May', 'days': 31},
        6: {'month': 'June', 'days': 30},
        7: {'month': 'July', 'days': 31},
        8: {'month': 'August', 'days': 31},
        9: {'month': 'September', 'days': 30},
        10: {'month': 'October', 'days': 31},
        11: {'month': 'November', 'days': 30},
        12: {'month': 'December', 'days': 31}
    }
    i = 1
    days_total = 0
    while True:
        if leapyear(year) and i == 2:
            days_total = days_total + 29
        else:
            days_total = days_total + days_in_month[i]['days']
        if days_total >= day:
            break
        else:
            i += 1
    month = days_in_month[i]['month']
    day_of_month = day - (days_total - days_in_month[i]['days'])
    return day_of_month, month, year

if __name__ == "__main__":
    main()