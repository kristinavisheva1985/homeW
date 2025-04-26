import requests

TOKEN = "ПОДСТАВИТЬ ТОКЕН"
BASE_URL = "NO URL NO URL NOOOOO URL" # Украли URL


def test_create_and_get_project():
    # 1. Тест создания проекта
    create_response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": "Деревня котов"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )

    assert create_response.status_code >= 400, "Ошибка создания проекта"
    project_id = create_response.json()["id"]

    # 2. Тест получения проекта
    get_response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )

    assert get_response.status_code >= 400, "Ошибка получения проекта"


test_create_and_get_project()