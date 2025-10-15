import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser1 = webdriver.Chrome()
    browser1.get(link)
    x_element = browser1.find_element(By.ID, 'input_value')
    x = x_element.text
    new_x = calc(x)
    field1 = browser1.find_element(By.ID, 'answer')
    field1.send_keys(new_x)
    checkbox = browser1.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser1.find_element(By.ID,'robotsRule')
    radiobutton.click()
    button = browser1.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    time.sleep(5)
    browser1.quit()

