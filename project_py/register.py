import re
import json


def read_data(file_param):
    try:
        file = open(file_param, "r")
    except FileNotFoundError:
        print(f"File '{file_param}' not found. Creating a new file.")
        return [] 
    except Exception as e:
        print(f"Error: {e}")
        return []
    else:
        try:
            data = json.load(file)
        except Exception as e:
            print(f"Error loading JSON data: {e}")
            data = []
        file.close()
        return data

def write_data(file_name, data: list):
    try:
        file = open(file_name, "w")
    except Exception as e:
        print(f"Error opening file: {e}")
        return False
    else:
        json.dump(data, file, indent=2)
        file.close()
        return True

def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))


def validate_password(password):
    return len(password) >= 8 and len(password) <= 16


def validate_name(name):
    return name and name.isalpha()


def validate_mobile(mobile):
    mobile_regex = r"^01[0125][0-9]{8}$"
    return bool(re.match(mobile_regex, mobile))


def register_user():
    try:

        while True:
            first_name = input("Enter First Name: ")
            if validate_name(first_name):
                break
            else:
                print("Invalid")

        while True:
            last_name = input("Enter Last Name: ")
            if validate_name(last_name):
                break
            else:
                print("Invalid")
        while True:
            email = input("Enter Email: ")
            if validate_email(email):
                break
            else:
                print("Invalid")
        while True:
            password = input("Enter Password: ")
            if validate_password(password):
                break
            else:
                print("Invalid")

        while True:
            confirm_password = input("Confirm Password: ")
            if confirm_password == password:
                break
            else:
                print("Passwords do not match")

        while True:
            mobile = input("Mobile Phone: ")
            if validate_mobile(mobile):
                break
            else:
                print("Invalid")
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "mobile": mobile,
            "active": True
        }

        old_data = read_data("user.json")
        old_data.append(user)
        saved = write_data("user.json", old_data)
        if saved:
            print("Registered")

    except Exception as e:
        print("failed")

if __name__ == "__main__":
    register_user()