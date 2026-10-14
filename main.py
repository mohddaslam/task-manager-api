from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_connection, create_table

app = FastAPI()

# Create the database table when the API starts
create_table()


class Task(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "Welcome to my Task Manager API!"}


@app.get("/tasks")
def get_tasks():
    connection = get_connection()
    tasks = connection.execute(
        "SELECT * FROM tasks"
    ).fetchall()
    connection.close()

    return [dict(task) for task in tasks]


@app.post("/tasks")
def add_task(task: Task):
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (task.title, task.completed)
    )
    connection.commit()

    new_task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (cursor.lastrowid,)
    ).fetchone()
    connection.close()

    return dict(new_task)


@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )
    connection.commit()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()
    connection.close()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return dict(task)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
