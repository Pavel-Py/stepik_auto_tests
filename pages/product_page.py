from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        """
        Добавляет товар в корзину.
        """
        add_basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        add_basket_link.click()
        self.solve_quiz_and_get_code()

    def compare_prod_name_and_basket_message_name(self):
        """
        Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        """
        prod_name_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PROD_NAME).text
        prod_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        assert prod_name_in_alert == prod_name

    def compare_prod_price_and_basket_message_price(self):
        """
        Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        prod_price = self.browser.find_element(*ProductPageLocators.PROD_PRICE).text
        prod_price_from_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PROD_PRICE).text
        assert prod_price == prod_price_from_message

    def should_not_be_success_message(self):
        """
        Проверяет отсутствие элемента на странице.
        """
        assert self.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE_PROD_NAME), \
            'Сообщение о добавлении в корзину появилось, хотя не должно было'

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_MESSAGE_PROD_NAME)
