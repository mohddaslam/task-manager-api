# Task Manager API

A beginner backend development project built with Python, FastAPI, and SQLite. This REST API allows users to create, retrieve, update, and delete tasks.

## Live Demo

- **Live API:** https://task-manager-api-vv87.onrender.com
- **Interactive API Documentation (Swagger):** https://task-manager-api-vv87.onrender.com/docs
- **GitHub Repository:** https://github.com/mohddaslam/task-manager-api

> Note: The free Render service may take some time to respond after inactivity. SQLite data may be lost when the service restarts or is redeployed.

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
- Cloud deployment using Render

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- SQLite
- Pytest
- Docker
- Git and GitHub
- Render

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a task |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

You can try these endpoints using the [live Swagger documentation](https://task-manager-api-vv87.onrender.com/docs).

## Run Locally

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Start the API

```bash
uvicorn main:app --reload
```

### 3. Open the documentation

Visit http://localhost:8000/docs

## Run Tests

```bash
python -m pytest -v
```

The project's automated test suite passed all 7 tests during local testing.

## Run with Docker

Build the production Docker image:

```bash
docker build -f Dockerfile.prod -t task-manager-api .
```

Start the container:

```bash
docker run -d --name task-manager-container -p 8000:8000 -v task-manager-data:/app/data task-manager-api
```

Open http://localhost:8000/docs to access the API.

To stop the container:

```bash
docker stop task-manager-container
```

To remove the stopped container:

```bash
docker rm task-manager-container
```

The named Docker volume stores the SQLite database outside the container, helping preserve local data when the container is removed and recreated.

## Database

The application uses SQLite to store tasks. The database path is configured through the `DATABASE_PATH` environment variable.

For the Render free deployment, do
