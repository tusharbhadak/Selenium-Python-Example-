from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("https://www.google.com")

driver.find_element("name", "q").send_keys("sdjic")
time.sleep(3)

driver.find_element("name", "btnK").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
print("Sample test case successfully completed")