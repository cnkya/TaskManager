import requests

URL = "http://127.0.0.1:5000/tasks"

def update_task(name, summary, description):
    task_data = {
        "name":name,
        "summary":summary,
        "description":description
    }
    response = requests.put(URL, json=SOMEDATA)
    if response.status_code == 204:
        print("Task successfully updated")
    else:
        print("Task update failed")

if __name__ == "__main__":
    print("Update a task by filling out the prompts below:")
    name = input("Task name: ")
    summary = input("Task summary: ")
    description = input("Task description: ")
    update_task(name, summary, description)