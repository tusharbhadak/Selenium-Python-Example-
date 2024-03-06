from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://badmintoncorner.com/account/register")
driver.get("https://badmintoncorner.com/account/login?return_url=%2Faccount")
time.sleep(2)

# signup
# driver.find_element("id","FirstName").send_keys("Harshit")
# driver.find_element("id","LastName").send_keys("Gupta")
# driver.find_element("id","Email").send_keys("xerecev999@locawin.com")
# driver.find_element("id","CreatePassword").send_keys("xerecev999")

# login
driver.find_element("id", "CustomerEmail").send_keys("xerecev999@locawin.com")
driver.find_element("id", "CustomerPassword").send_keys("xerecev999")

time.sleep(2)
driver.find_element(By.CLASS_NAME,"btn").click()

time.sleep(4)
driver.close()
