from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#input_value")
    x = num1.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 150);")

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    click_check = browser.find_element_by_css_selector("#robotCheckbox")
    click_check.click()
    click_check = browser.find_element_by_css_selector("#robotsRule")
    click_check.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)

    browser.quit()