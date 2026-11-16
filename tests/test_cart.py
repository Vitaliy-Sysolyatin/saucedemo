import allure

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@allure.title("Проверка товара в корзине")
@allure.description(
    "Авторизация в SauceDemo, добавление товара и проверка его "
    "названия и цены в корзине."
)
def test_product_data_in_cart(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)

    login_page.open(login_page.URL)
    login_page.login(USERNAME, PASSWORD)

    product_name = inventory_page.get_product_name()
    product_price = inventory_page.get_product_price()

    inventory_page.add_backpack()
    inventory_page.open_cart()

    assert cart_page.get_product_name() == product_name
    assert cart_page.get_product_price() == product_price