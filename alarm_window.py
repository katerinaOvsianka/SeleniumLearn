from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser5 = webdriver.Chrome()
link = 'https://suninjuly.github.io/alert_accept.html'
browser5.get(link)
button = browser5.find_element(By.CLASS_NAME, 'btn')
button.click()
alarm = browser5.switch_to.alert
alarm.accept()
x = browser5.find_element(By.ID, 'input_value').text
new_x = calc(x)
fieldx = browser5.find_element(By.ID, 'answer')
fieldx.send_keys(new_x)
button1 = browser5.find_element(By.CLASS_NAME, 'btn')
button1.click()
time.sleep(5)


