from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num1 = browser.find_element_by_css_selector("#input_value")
    x = num1.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)

    browser.quit()