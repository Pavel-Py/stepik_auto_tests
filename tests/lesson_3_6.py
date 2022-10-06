import math
import pytest
import time
from selenium.webdriver.common.by import By

numbers = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.mark.parametrize('url_pk', numbers)
def test_parametrize(browser, url_pk):
    browser.implicitly_wait(5)
    browser.get(f'https://stepik.org/lesson/{url_pk}/step/1')
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder]').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert text == 'Correct!'
