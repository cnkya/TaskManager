from flask import (
    Flask,
    request

)
from app.database import task

app = Flask(__name__)

#HTTP GET METHOD
@app.get("/tasks")
def get_all_tasks():
    tasks_list = task.scan()
    out = {
        "tasks" : tasks_list,
        "ok":True
    }
    return out
   

@app.get("/tasks/<int:pk>/")# pk stands for parameter key#
def get_single_task(pk):
    single_task = task.select_by_id(pk)
    if single_task:
        out = {
            "tasks":single_task,
            "ok":True
        }
    return out

    out = {
     "ok":False,
    "message":"Not Found"

    }
    return out, 404

#HTTP POST METHODS
@app.post("/tasks")
def create_task():
    tasks_data = request.json
    task.insert(tasks_data)
    return "", 204

#HTTP PUT METHODS
@app.put("/tasks/<int:pk>/")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data,pk)
    return "", 204

#HTTP DELETE METHODS
@app.delete ("/tasks/<int:pk>/")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204