import datetime
import json


def validate_datetime(input_date):
    try:
        date_obj = datetime.datetime.strptime(input_date, '%d/%m/%Y')
        return date_obj
    except ValueError:
        print("Invalid")
        return None


def target_amount(amount):
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            print("Total target must be a positive number.")
            return None
        return amount_float
    except ValueError:
        print("Invalid")
        return None


def create_project(user_name):
    try:
        title = input("title: ")
        details = input("details: ")
        total_target = input("target amount: ")
        total_target = target_amount(total_target)
        if total_target is None:
            return None

        start_date = input("start date: ")
        start_date = validate_datetime(start_date)
        if start_date is None:
            return None

        end_date = input("end date ")
        end_date = validate_datetime(end_date)
        if end_date is None:
            return None

        if end_date <= start_date:
            return None

        project_data = {
            "Title": title,
            "Details": details,
            "Total_Target": total_target,
            "Start_Date": start_date.strftime('%d/%m/%Y'),
            "End_Date": end_date.strftime('%d/%m/%Y'),
            "User": user_name
        }

        return project_data
    except Exception as e:
        print("Error occurred while creating project:", e)
        return None


def save_project(project_data):
    try:
        try:
            file = open("project.json", 'r')
            existing_projects = json.load(file)
            file.close()
        except (FileNotFoundError, json.JSONDecodeError):
            existing_projects = []

        existing_projects.append(project_data)
        file = open("project.json", 'w')
        json.dump(existing_projects, file, indent=2)
        file.close()
        print("saved successfully")
    except Exception as e:
        print("Error", e)


def main(user_name):
    try:
        project_data = create_project(user_name)
        if project_data:
            save_project(project_data)
        else:
            print("try again")
    except Exception as e:
        print("Error ", e)


if __name__ == "__main__":
    main(user_name="")