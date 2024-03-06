from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/gupta/Downloads/python-selenium/registration.html")

time.sleep(1)

# text box
driver.find_element(By.NAME, "fname").send_keys("Harshit")
driver.find_element(By.NAME, "lname").send_keys("Gupta")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "phNo").send_keys("7687543456")

# radio
driver.find_element(By.ID, "male").click()

# checkbox
driver.find_element(By.NAME, "bca").click()
driver.find_element(By.NAME, "mca").click()

# select
degree = Select(driver.find_element(By.ID, "country"))
degree.select_by_visible_text("India")

# multi select
hobbies = Select(driver.find_element(By.ID, "hobbies"))
hobbies.select_by_visible_text("Reading")
hobbies.select_by_visible_text("Singing")

# textbox
driver.find_element(By.NAME, "address").send_keys("Vesu")

# file
file_input =  driver.find_element(By.NAME, "profile_pic")
file_path = "C:/Users/gupta/Downloads/photopea.png"
file_input.send_keys(file_path)

time.sleep(5)

driver.close()