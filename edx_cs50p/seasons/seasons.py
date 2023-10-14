from datetime import date
import inflect
import sys


def main():

    p = inflect.engine()
    dob_y, dob_m, dob_d = get_dob()
    dob = date(dob_y, dob_m, dob_d)
    today = date.today()
    dob_timedelta = today - dob

    minutes_since_birth = dob_timedelta.days * 24 * 60

    print(f'{p.number_to_words(minutes_since_birth, andword="").capitalize()} minutes')


def get_dob():
    rv = []
    rv_dob = input("Date of Birth (YYYY-MM-DD): ")
    if len(rv_dob.split("-")) != 3:
        sys.exit("Invalid date")
    try:
        for part in rv_dob.split("-"):
            rv.append(int(part))
    except ValueError:
        sys.exit("Invalid date")
    else:
        return rv

if __name__ == "__main__":
    main()