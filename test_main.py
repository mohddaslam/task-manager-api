
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_homepage():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to my Task Manager API!"
    }

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Automated test task",
            "completed": False
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Automated test task"
    assert response.json()["completed"] == 0

def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old title",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    update_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "New title",
            "completed": True
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["title"] == "New title"
    assert update_response.json()["completed"] == 1

    assert update_response.status_code == 200
    assert update_response.json()["title"] == "New title"
    assert update_response.json()["completed"] == 1


def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task to delete",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/tasks/{task_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json() == {
        "message": "Task deleted successfully"
    }
