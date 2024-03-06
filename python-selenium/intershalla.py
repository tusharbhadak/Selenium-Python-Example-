from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://internshala.com/")

element = driver.find_element("link text", "Hire Talent").click()
time.sleep(2)

element = driver.find_element("id","email").send_keys("abc@gmail.com")
time.sleep(2)

element = driver.find_element("id","password").send_keys("password")
time.sleep(2)

element = driver.find_element("id","first_name").send_keys("Harshit")
time.sleep(2)

element = driver.find_element("id","last_name").send_keys("Gupta")
time.sleep(2)

element = driver.find_element("id","phone_primary").send_keys("1898767564")
time.sleep(2)

element = driver.find_element("id", "job_employer_registration_button").click()
time.sleep(2)

action = ActionChains(driver)

action.click(on_element= element)

driver.close()