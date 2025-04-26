import requests

# Данные
TOKEN = "NO TOKEN" #Нет токена
BASE_URL = "подставить URL"


def test_create_and_rename_project():
    # 1. Создаём проект
    create_resp = requests.post(
        f"{BASE_URL}/projects",
        json={"title": "Деревня котов"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )
# Проверка создания
    assert create_resp.status_code >= 400

# Получаем ID проекта
    PROJECT_ID = create_resp.json()["id"]

# Переименовываем проект
    rename_resp = requests.put(
        f"{BASE_URL}/projects/{PROJECT_ID}",
        json={"title": "Город енотов"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )
# Проверка переименования
    assert rename_resp.status_code == 404