Diplom
Автоматизация тестирования на python
Структура проекта (описание файлов и что в них расположено):
config.py - в файле расположены данные для api и ui тестов
conftest.py - основные команды открытия, перехода на страницу тестируемого приложения, ожидания и закрытия браузера, для всех тестов
ui_client.py - классы, локаторы и методы ui-тестов
api_client.py - классы и методы api-тестов
test_api_py - api-тесты
test_ui.py - ui-тесты
Шаги:
Склонировать проект 'git clone https://github.com/Demero-art/DiploSky.git'

Установить все зависимости 'pip install -r requirements.txt'

Запустить тесты: 'pytest'

Сгенерировать отчет: 'allure generate allure-files -o allure-report'

Открыть отчет: 'allure open allure-report'

Стек:
pytest

selenium

requests

allure

config