from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-price']"
    )

    def get_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.driver.find_element(*self.PRODUCT_PRICE).text
