from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_MESSAGE_PROD_NAME = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1) strong')
    PROD_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PROD_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_MESSAGE_PROD_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
