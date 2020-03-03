from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1")
    x = int(num1.text)

    num2 = browser.find_element_by_css_selector("#num2")
    y = int(num2.text)

    z = str(x + y)

    dropD = Select(browser.find_element_by_tag_name("select"))
    dropD.select_by_visible_text(z)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)

    browser.quit()