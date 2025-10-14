import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from find_element import browser

link = "https://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for elements in elements:
      elements.send_keys("hello")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
