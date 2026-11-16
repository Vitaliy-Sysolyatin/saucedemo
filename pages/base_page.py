from selenium.webdriver.common.by import By


class BasePage:
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def open_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()
