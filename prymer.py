import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, 'input_value').text
new_x = calc(x)
fieldx = browser.find_element(By.ID, 'answer')
fieldx.send_keys(new_x)
check = browser.find_element(By.ID, 'robotCheckbox')
check.click()
radio = browser.find_element(By.ID, 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()
button = browser.find_element(By.CLASS_NAME, 'btn')
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)

