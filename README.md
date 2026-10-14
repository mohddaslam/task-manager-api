
# Task Manager API

A beginner backend development project built with Python, FastAPI, and SQLite. The application provides REST API endpoints to create, retrieve, update, and delete tasks.

## Features

- Create new tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update existing tasks
- Delete tasks
- Validate task titles
- Return appropriate errors for tasks that do not exist
- Automated API tests using pytest
- Docker support for containerized execution

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- SQLite
- Pytest
- Docker
- Git and GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a task |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Run Locally

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

http://localhost:8000/docs

## Run Tests

```bash
python -m pytest -v
```

## Run with Docker

Build the Docker image:

```bash
docker build -t task-manager-api .
```

Start the container:

```bash
docker run -d --name task-manager-container -p 8000:8000 task-manager-api
```

Open http://localhost:8000/docs to access the API.

To stop the container:

```bash
docker stop task-manager-container
```

## Database

The application uses SQLite to store tasks in `tasks.db`.

## Project Status

This is a learning and portfolio project. Further improvements may include cloud deployment, configuration management, and production security.
