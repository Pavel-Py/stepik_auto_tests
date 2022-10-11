from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REG_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_REG_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASS_REG_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
