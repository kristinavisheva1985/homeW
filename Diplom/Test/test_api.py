import allure
import requests
import sys
from pathlib import Path
import pytest
from pages.api_client import MarketDeliveryApiClient
from config import (CATEGORIES_PAYLOAD,
                    PRODUCT_PAYLOAD, CART_PARAMS, CART_PAYLOAD)


# Добавляем корневую директорию в путь поиска модулей
sys.path.append(str(Path(__file__).parent.parent))


@pytest.fixture
def api_client():
    return MarketDeliveryApiClient()


@allure.id("DELIVERY API")
@allure.feature('Позитивные API тесты')
@allure.story('Проверка получения списка категорий продуктов')
@pytest.mark.api
def test_get_categories_api(api_client):

    with allure.step("Отправка GET-запроса на получение категорий"):
        response_data = api_client.get_categories(CATEGORIES_PAYLOAD)

    with allure.step("Проверка структуры ответа"):
        assert isinstance(response_data, dict), "Должен быть JSON"
        assert "categories" in response_data, "Отсутствует ключ 'categories'"
        assert isinstance(response_data["categories"], list), "'categories' это список"
        assert len(response_data["categories"]) > 0, "Список категорий пуст"


@allure.id("DELIVERY API")
@allure.feature('Позитивные API тесты')
@allure.story('Проверка получения информации о продукте магазина')
@pytest.mark.api
def test_get_store_product_info(api_client):

    with allure.step("Отправка GET-запроса на получение информации о продукте"):
        response_data = api_client.get_product_info(PRODUCT_PAYLOAD)

    with allure.step("Проверка наличия и валидности данных о категориях товара"):
        assert isinstance(response_data, dict), "Ответ должен быть JSON-объектом"
        if PRODUCT_PAYLOAD["with_categories"]:
            assert "categories" in response_data, "Не получены категории"
            assert isinstance(response_data["categories"], list), "Категории должны быть списком"


@allure.id("DELIVERY API")
@allure.feature('Позитивные API тесты')
@allure.story('Добавление товара в корзину')
@pytest.mark.api
def test_add_to_cart(api_client):

    with allure.step("Отправка POST-запроса на добавление товара в корзину"):
        response_data = api_client.add_to_cart(CART_PAYLOAD, CART_PARAMS)

    with allure.step("Проверка структуры ответа"):
        assert isinstance(response_data, dict), "Ответ должен быть JSON-объектом"
        assert "cart" in response_data, "В ответе должна быть информация о корзине"


@allure.id("DELIVERY API")
@allure.feature('Негативные API тесты')
@allure.story('Проверка некорректного URL при получении информации о продукте')
@pytest.mark.api
def test_invalid_url_product_info(api_client):

    with allure.step("Отправка GET-запроса с неправильным URL"):
        try:
            api_client.get_product_info(PRODUCT_PAYLOAD, invalid_url=True)
            pytest.fail("Ожидалась ошибка 400")
        except requests.exceptions.HTTPError as e:
            with allure.step("Проверка статуса и формата ошибки"):
                assert e.response.status_code == 400, f"Ожидался статус 400, получен {e.response.status_code}"
                error_data = e.response.json()
                assert isinstance(error_data, dict), "Ответ об ошибке должен быть JSON-объектом"
                assert "message" in error_data or "error" in error_data, "Должно быть описание ошибки"


@allure.id("DELIVERY API")
@allure.feature('Негативные API тесты')
@allure.story('Отправка POST-запроса с пустым (невалидным) телом')
@pytest.mark.api
def test_empty_body_request(api_client):

    with allure.step("Отправка POST-запроса с пустым телом"):
        with pytest.raises(requests.exceptions.HTTPError) as err:
            api_client.post_product_with_empty_body()

    with allure.step("Проверка статуса и формата ответа"):
        resp = err.value.response
        data = resp.json()
        assert resp.status_code == 400, f"Получен неверный статус-код: {resp.status_code}, ожидалось 400."
        assert isinstance(data, dict), "Ответ должен прийти в виде JSON-объекта."