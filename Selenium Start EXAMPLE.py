from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()

# https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python

# https://www.selenium.dev/documentation/overview/ 