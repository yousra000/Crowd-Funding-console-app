import json
from register import validate_email, validate_password
from crud.updatep import edit
from crud.deletep import delete
from crud.createp import main
from crud.viewp import view_projects
from crud.searching import search_projects_by_date


def login():
    try:
        while True:
            email = input("Email: ")
            if validate_email(email):
                break
            else:
                print("Invalid email. Please try again.")
        while True:
            password = input("Password: ")
            if validate_password(password):
                break
            else:
                print("Invalid Password. Please try again.")

        try:
            with open("user.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []

        for user in users:
            if user["email"] == email and user["password"] == password and user["active"] == True:
                print("Login successful")
                login_menu(user["first_name"])
                return

        raise ValueError("Invalid email or password")
    except ValueError as e:
        print("Login failed: " + str(e))


def login_menu(user_name):
    if user_name:
        while True:
            choice = int(input("""
                1- Create new project      
                2- View all projects
                3- Edit project            
                4- Delete project
                5- Search_projects_by_date
                6- Logout
                """))

            if choice == 1:
                main(user_name)
            elif choice == 2:
                view_projects() 
            elif choice == 3:
                edit(user_name)
            elif choice == 4:
                delete(user_name)
            elif choice == 5:
                date_str = input("date (YYYY-MM-DD)")
                search_projects_by_date(date_str)
            elif choice == 6:
                return


if __name__ == "__main__":
    login()