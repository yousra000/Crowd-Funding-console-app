import json


def delete_project(user_name):
    try:
        f = open("project.json", 'r')
        projects = json.load(f)
        f.close()
    except FileNotFoundError:
        print("No projects found.")
        return

    user_projects = []
    for project in projects:
        if project.get("User") == user_name:
            user_projects.append(project)

    if not user_projects:
        print("no projects to delete.")
        return

    print("Your Projects:")
    for idx, project in enumerate(user_projects, start=1):
        print(f"{idx}. {project['Title']}")

    selection = input("num of the project: ")
    try:
        selection = int(selection)
        if selection < 1 or selection > len(user_projects):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return

    del projects[projects.index(user_projects[selection - 1])]

    f = open("project.json", 'w')
    json.dump(projects, f, indent=2)
    f.close()

    print("deleted successfully")


def delete(user_name):
    try:
        delete_project(user_name)
    except Exception as e:
        print("An error occurred:", e)