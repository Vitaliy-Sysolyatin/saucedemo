import allure

from selenium.webdriver.common.by import By

SAUCEDEMO_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@allure.title("Проверка локаторов страницы авторизации")
@allure.description(
    "Поиск основных локаторов,xpath и css-селекторов на странице авторизации"
)
def test_login_page_locators(browser):
    browser.get(SAUCEDEMO_URL)

    # Основные стратегии локаторов

    browser.find_element(By.ID, "user-name")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CLASS_NAME, "login_logo")
    browser.find_element(By.TAG_NAME, "input")

    # XPath по атрибуту

    browser.find_element(
        By.XPATH,
        "//input[@id='user-name']"
    )

    # XPath contains для атрибута

    browser.find_element(
        By.XPATH,
        "//input[contains(@id, 'user')]"
    )

    # XPath с двумя условиями

    browser.find_element(
        By.XPATH,
        "//input[@name='user-name' and @type='text']"
    )

    # XPath parent

    browser.find_element(
        By.XPATH,
        "//input[@id='user-name']/parent::*"
    )

    # XPath preceding

    browser.find_element(
        By.XPATH,
        "//input[@id='password']"
        "/preceding::input[@id='user-name'][1]"
    )

    # CSS .class

    browser.find_element(
        By.CSS_SELECTOR,
        ".login_logo"
    )

    # CSS .class1.class2

    browser.find_element(
        By.CSS_SELECTOR,
        ".submit-button.btn_action"
    )

    # CSS #id

    browser.find_element(
        By.CSS_SELECTOR,
        "#user-name"
    )

    # CSS tagname

    browser.find_element(
        By.CSS_SELECTOR,
        "input"
    )

    # CSS tagname.class

    browser.find_element(
        By.CSS_SELECTOR,
        "input.form_input"
    )

    # CSS [attribute=value]

    browser.find_element(
        By.CSS_SELECTOR,
        "input[name='user-name']"
    )

    # CSS [attribute~=value]

    browser.find_element(
        By.CSS_SELECTOR,
        "input[class~='form_input']"
    )

    # CSS [attribute|=value]

    browser.find_element(
        By.CSS_SELECTOR,
        "input[id|='user']"
    )

    # CSS [attribute^=value]

    browser.find_element(
        By.CSS_SELECTOR,
        "input[id^='user']"
    )

    # CSS [attribute$=value]

    browser.find_element(
        By.CSS_SELECTOR,
        "input[id$='name']"
    )

    # CSS [attribute*=value]

    browser.find_element(
        By.CSS_SELECTOR,
        "input[id*='user']"
    )


@allure.title("Проверка локаторов страницы inventory")
@allure.description(
    "Поиск основных локаторов,xpath и css-селекторов на странице inventory"
)
def test_inventory_page_locators(browser):
    browser.get(SAUCEDEMO_URL)

    # Авторизация

    browser.find_element(
        By.ID,
        "user-name"
    ).send_keys(USERNAME)

    browser.find_element(
        By.ID,
        "password"
    ).send_keys(PASSWORD)

    browser.find_element(
        By.ID,
        "login-button"
    ).click()

    # CSS .class1 .class2

    browser.find_element(
        By.CSS_SELECTOR,
        ".inventory_list .inventory_item"
    )

    # LINK_TEXT

    browser.find_element(
        By.LINK_TEXT,
        "Sauce Labs Backpack"
    )

    # PARTIAL_LINK_TEXT

    browser.find_element(
        By.PARTIAL_LINK_TEXT,
        "Sauce Labs"
    )

    # XPath по тексту

    browser.find_element(
        By.XPATH,
        "//div[text()='Sauce Labs Backpack']"
    )

    # XPath contains для текста

    browser.find_element(
        By.XPATH,
        "//div[contains(text(), 'Backpack')]"
    )

    # XPath contains для атрибута

    browser.find_element(
        By.XPATH,
        "//button[contains(@id, 'add-to-cart')]"
    )

    # XPath ancestor

    browser.find_element(
        By.XPATH,
        "//*[contains(@class, 'inventory_item_name')]"
        "/ancestor::*[contains(@class, 'inventory_item')][1]"
    )

    # XPath descendant

    browser.find_element(
        By.XPATH,
        "//*[contains(@class, 'inventory_item')][1]"
        "/descendant::*[contains(@class, 'inventory_item_price')]"
    )

    # XPath following

    browser.find_element(
        By.XPATH,
        "//*[contains(@class, 'inventory_item_name')]"
        "/following::*[contains(@class, 'inventory_item_price')][1]"
    )