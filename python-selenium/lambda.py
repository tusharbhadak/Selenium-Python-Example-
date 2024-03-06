from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://lambdatest.github.io/sample-todo-app/")
time.sleep(2)

driver.find_element("id","sampletodotext").send_keys("Python")
driver.find_element("id","addbutton").click()

time.sleep(2)
driver.find_element("name","li3").click()

time.sleep(4)
driver.close()
