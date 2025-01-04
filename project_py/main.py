from login import login
from register import register_user


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                register_user()
            elif choice == "2":
                login()
            elif choice == "3":
                print("See you later...")
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("Error: " + str(e))


if __name__ == "__main__":
    main()