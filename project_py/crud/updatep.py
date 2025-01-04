import json

def edit_project(user_name):
    try:
        with open("project.json", "r") as file:
            projects = json.load(file)

        user_projects = [project for project in projects if project.get("User") == user_name]

        if not user_projects:
            print(f"No projects found for user '{user_name}'.")
            return

        print("Your Projects:")
        for idx, project in enumerate(user_projects, start=1):
            print(f"{idx}. {project['Title']}")

        selection = input("Enter the number of the project to edit: ")
        try:
            selection = int(selection)
            if selection < 1 or selection > len(user_projects):
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            return

        selected_project = user_projects[selection - 1]
        selected_project["Title"] = input(f"New Title ({selected_project['Title']}): ") or selected_project["Title"]
        selected_project["Details"] = input(f"New Details ({selected_project['Details']}): ") or selected_project["Details"]
        selected_project["Total_Target"] = input(f"New Total Target ({selected_project['Total_Target']}): ") or selected_project["Total_Target"]
        selected_project["Start_Date"] = input(f"New Start Date ({selected_project['Start_Date']}): ") or selected_project["Start_Date"]
        selected_project["End_Date"] = input(f"New End Date ({selected_project['End_Date']}): ") or selected_project["End_Date"]

        with open("project.json", "w") as f:
            json.dump(projects, f, indent=2)

        print("Project updated successfully.")

    except FileNotFoundError:
        print("No projects found")
    except Exception as e:
        print("An error occurred:", e)


def edit(user_name):
    try:
        edit_project(user_name)
    except Exception as e:
        print("An error occurred:", e)

