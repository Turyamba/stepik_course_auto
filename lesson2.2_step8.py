from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("123")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("123")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("123")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input_file = browser.find_element_by_name("file")
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(5)

    browser.quit()