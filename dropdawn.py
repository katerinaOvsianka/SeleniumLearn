import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link3 = 'https://suninjuly.github.io/selects1.html'
    browser3 = webdriver.Chrome()
    browser3.get(link3)
    first_num = browser3.find_element(By.ID, 'num1').text
    second_num = browser3.find_element(By.ID, 'num2').text
    summ = str(int(first_num) + int(second_num))
    print(summ)
    # dropdown = browser3.find_element(By.ID, 'dropdown')
    dropdown = Select(browser3.find_element(By.ID, 'dropdown'))
    dropdown.select_by_value(summ)
    find_button = browser3.find_element(By.CSS_SELECTOR, 'button.btn')
    find_button.click()
finally:
    time.sleep(5)