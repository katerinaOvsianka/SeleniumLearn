import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CLASS_NAME, "first")
    first_name.send_keys('buba')
    last_name = browser.find_element(By.CLASS_NAME, "second")
    last_name.send_keys('bubaev')
    email = browser.find_element(By.CLASS_NAME, "third")
    email.send_keys('bubaev@frum.rum')

finally:
    time.sleep(6)
