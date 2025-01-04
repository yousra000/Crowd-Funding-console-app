import json


def view_projects():
    try:
        f = open("project.json", 'r')
        projects = json.load(f)
        f.close()

        if projects:
            print("All Projects:")
            for idx, project in enumerate(projects, start=1):
                print(f"\nProject {idx}:")
                print("Title:", project["Title"])
                print("Details:", project["Details"])
                print("Total Target:", project["Total_Target"])
                print("Start Date:", project["Start_Date"])
                print("End Date:", project["End_Date"])
        else:
            print("No projects found.")
    except FileNotFoundError:
        print("No projects found.")