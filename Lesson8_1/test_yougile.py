import requests

# Данные
TOKEN = "TOKEN"
BASE_URL = "URL"


def test_project_creation():
    # Отправляем запрос на создание проекта
    resp = requests.post(
        f"{BASE_URL}/projects",
        json={"title": "Деревня гусей"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )

    # Проект создался
    assert resp.status_code == 201