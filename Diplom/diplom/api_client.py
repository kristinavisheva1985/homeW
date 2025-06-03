import requests
from typing import Dict, Any
import allure


class MarketDeliveryApiClient:
    BASE_URL = "https://market-delivery.yandex.ru/api"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    @allure.step("Получить категории товаров")
    def get_categories(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/v2/menu/goods/get-categories?auto_translate=false"
        return self._make_request("POST", url, json=payload)

    @allure.step("Получить информацию о продукте")
    def get_product_info(self, payload: Dict[str, Any], invalid_url: bool = False) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/v2/menu/product?auto_translate={'false' if not invalid_url else 'fals'}"
        return self._make_request("POST", url, json=payload)

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self, payload: Dict[str, Any], params: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/v1/cart"
        return self._make_request("POST", url, json=payload, params=params)

    @allure.step("Отправить POST-запрос с пустым телом")
    def post_product_with_empty_body(self):
        endpoint = "/v2/menu/product?auto_translate=false"
        full_url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(full_url, json=None)
        response.raise_for_status()  # Поднимет исключение, если произошла ошибка
        return response

    @allure.step("Выполнить HTTP-запрос")
    def _make_request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()