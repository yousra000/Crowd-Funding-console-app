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

def search_projects_by_date(date_str):

    projects = read_data("project.json")
    found_projects = []

    for project in projects:
        if project["Start_Date"] == date_str:
            found_projects.append(project)
    
    if found_projects:
        for project in found_projects:
            print(f"Name: {project['Title']}\nDetails: {project['Details']}\n")
    else:
        print("No projects found")
