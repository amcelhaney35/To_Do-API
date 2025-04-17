#main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to your To-Do API!"}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

#In-memory database
tasks = []
task_id_counter = 1

# Data model for a Task
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    
# Create a task
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    global task_id_counter
    task.id = task_id_countertask_id_counter += 1
    tasks.append(task)
    return task

#Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

#Get a single task by ID
@app.get("/tasks{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
     raise HTTPExceptions(status_code=404, detail="Task not found")
 
#Update a task
@app.put("/task/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated_task.id = task_id
            tasks[i] = updated_task
            return updated_task
     raise HTTPException(status_code=404, detail="Task not found")
 
 #Delete a task
 @app.delete("/tasks/{task_id}")
 def delete_task(task_id: int):
     for i, task in enumerate(tasks):
         if task.id == task_id:
             del tasks[i]
             return {"message": "Task deleted"
     raise HTTPException(status_code=404, detail="Task not found")}