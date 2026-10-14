
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
