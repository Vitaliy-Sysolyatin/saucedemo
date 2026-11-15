## Структура

- `pages/base_page.py` — общие для страниц элементы и действия.
- `pages/login_page.py` — авторизация.
- `pages/inventory_page.py` — работа с товаром.
- `pages/cart_page.py` — проверка товара в корзине.
- `tests/test_locators.py` — примеры стратегий локаторов.
- `tests/test_cart.py` — проверка добавления товара в корзину.
- `conftest.py` — фикстура браузера, настройки Chrome и скриншот при падении теста.

## Зависимости

```bash
pip install -r requirements.txt
```

Для формирования Allure-отчёта используется `allure-pytest`.

Для команды `allure serve` нужен Allure Commandline:

```bash
npm install -g allure-commandline
```

## Запуск

Обычный запуск:

```bash
pytest
```

Запуск с сохранением результатов Allure:

```bash
pytest --alluredir=allure-results
```

Открыть отчёт:

```bash
allure.cmd serve allure-results
```


## Настройки Chrome

В `conftest.py` отключён менеджер паролей Chrome:

- `credentials_enable_service = False`
- `profile.password_manager_enabled = False`

Также включён режим инкогнито и отключены уведомления, popup-блокировка и infobars.

При падении теста в Allure автоматически прикладывается скриншот браузера.