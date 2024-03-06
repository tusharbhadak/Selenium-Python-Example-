from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
time.sleep(2)

driver.find_element("name","search").send_keys("John Doe", Keys.ENTER)
time.sleep(2)

driver.close()