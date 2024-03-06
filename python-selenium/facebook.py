from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(3)

element = driver.find_element("id", "email").send_keys("")
time.sleep(3)

element = driver.find_element("id","pass").send_keys("")
time.sleep(10)

element = driver.find_element("name", "login").click()

action = ActionChains(driver)

action.perform()
