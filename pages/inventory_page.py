from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-price']"
    )
    ADD_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def get_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.driver.find_element(*self.PRODUCT_PRICE).text
