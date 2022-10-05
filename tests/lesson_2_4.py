from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    browser.find_element(By.ID, 'book').click()
    num = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.TAG_NAME, 'input').send_keys(log(abs(12 * sin(num))))
    browser.find_element(By.CSS_SELECTOR, '.container>button').click()
    print(browser.switch_to.alert.text)

browser.quit()

