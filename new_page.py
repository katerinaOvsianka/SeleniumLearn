import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/redirect_accept.html'
browser6 = webdriver.Chrome()
browser6.get(link)
button = browser6.find_element(By.CLASS_NAME,'trollface')
button.click()
new_window = browser6.window_handles[1]
browser6.switch_to.window(new_window)
x = browser6.find_element(By.ID, 'input_value').text
new_x = calc(x)
fieldx = browser6.find_element(By.ID, 'answer')
fieldx.send_keys(new_x)
button1 = browser6.find_element(By.CLASS_NAME, 'btn')
button1.click()

time.sleep(5)