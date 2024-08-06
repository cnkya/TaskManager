import requests

URL = "http://127.0.0.1:5000/tasks"

def delete_task(id):
    task_data = {
        "name":name,
        "summary":summary,
        "description":description
    }
    response = requests.delete(URL)
    if response.status_code == 204:
        print("Task successfully deleted")
    else:
        print("Task deletion failed")

if __name__ == "__main__":
    print("Delete a task by clicking 'delete' button")
    