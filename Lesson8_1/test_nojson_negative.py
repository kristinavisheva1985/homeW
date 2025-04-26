import requests

# Данные
TOKEN = "подставить данные"
BASE_URL = "подставить данные"


def test_project_creation():
    # Отправляем запрос на создание проекта
    resp = requests.post(
        f"{BASE_URL}/projects",
        json={"wrong_field" : "test"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )

    # Проект создался
    assert resp.status_code >= 400