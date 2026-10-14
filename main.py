from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_connection, create_table

app = FastAPI()

# Create the database table when the API starts
create_table()



from pydantic import BaseModel, Field, field_validator


class Task(BaseModel):
    title: str = Field(min_length=1)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Title cannot be empty or spaces")
        return value.strip()

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

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    connection = get_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return dict(task)

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
def update_task(task_id: int, updated_task: Task):
    connection = get_connection()

    cursor = connection.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (updated_task.title, updated_task.completed, task_id)
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
