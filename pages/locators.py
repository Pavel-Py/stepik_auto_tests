from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REG_FIELD = (By.ID, 'id_registration-email')
    PASS_REG_FIELD = (By.ID, 'id_registration-password1')
    REPEAT_PASS_REG_FIELD = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BASKET_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_MESSAGE_PROD_NAME = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1) strong')
    PROD_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PROD_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_MESSAGE_PROD_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')


class BasketPageLocators:
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '.basket-title')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
