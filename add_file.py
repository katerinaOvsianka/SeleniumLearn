import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file
print("Файл сохранён здесь:", os.path.abspath('test.txt'))

link = 'https://suninjuly.github.io/file_input.html'
browser4 = webdriver.Chrome()
browser4.get(link)
first_name = browser4.find_element(By.NAME, 'firstname')
last_name = browser4.find_element(By.NAME, 'lastname')
email = browser4.find_element(By.NAME, 'email')
first_name.send_keys('hello')
last_name.send_keys('hello')
email.send_keys('email@email.com')
add_file = browser4.find_element(By.ID, 'file')
current_dir = os.path.abspath(os.path.dirname(r'C:\Users\ekate\PycharmProjects\SeleniumLearn\test.txt'))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')
button = browser4.find_element(By.CLASS_NAME, 'btn')

add_file.send_keys(file_path)
button.click()
time.sleep(5)
