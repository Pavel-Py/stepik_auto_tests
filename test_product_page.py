import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize(
    'offer_num',
    [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='bug')) for i in range(10)]
)
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.compare_prod_name_and_basket_message_name()
    page.compare_prod_price_and_basket_message_price()
