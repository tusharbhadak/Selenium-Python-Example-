from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

driver.find_element(By.XPATH, "//button[@name='submit']").click()

alert = driver.switch_to.alert
time.sleep(2)
alert.accept()

time.sleep(2)

driver.close()