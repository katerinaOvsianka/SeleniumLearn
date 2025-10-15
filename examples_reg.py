import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    first_name.send_keys('buba')
    last_name = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    last_name.send_keys('bubaev')
    email = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    email.send_keys('bubaev@frum.rum')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    #time.sleep(3)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(6)
