from validator_collection import validators, checkers, errors

def main():
    user_email = input("What's your email? ")
    email_address = validate(user_email)
    if email_address == None:
        print("Invalid")
    else:
        print("Valid")

def validate(user_email):
    try:
        email_address = validators.email(user_email, allow_empty = True)
    except errors.EmptyValueError:
        return None
    except errors.InvalidEmailError:
        return None
    return email_address

if __name__ == "__main__":
    main()
