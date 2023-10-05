from validator_collection import checkers

def main():
    user_email = input("What's your email address? ").strip()
    print(check_email(user_email))

def check_email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()