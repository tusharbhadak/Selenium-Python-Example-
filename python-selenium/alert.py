from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
driver.get("file:///C:/Users/gupta/Downloads/python-selenium/alert.html")

try:
    driver.find_element("id",'simple').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")
    time.sleep(2)
    print("simple alert test passed")
    print("Now running prompt alert test")

try:
    driver.find_element("id",'prompt').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for prompt alert to appear')
    alert = driver.switch_to.alert
    alert.send_keys('560085')
    print("printing alert text")
    print(alert.text)
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")
    time.sleep(2)
    print("prompt alert test passed")
    print("Now running confirm alert test")

try:
    driver.find_element("id",'confirm').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for prompt alert to appear')
    alert = driver.switch_to.alert
    print("printing alert text from confirmation alert")
    print(alert.text)
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")
    time.sleep(2)
    print("confirmation alert test passed")

driver.quit()