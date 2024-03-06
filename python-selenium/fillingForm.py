from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iqssdss2020.pythonanywhere.com/tutorial/form/search")

driver.find_element(By.ID, "search_name").send_keys("Harshit Gupta")
time.sleep(2)

Select(driver.find_element(By.ID, "search_grade")).select_by_visible_text("2")
time.sleep(2)

driver.find_element(By.ID, "p10").click()
time.sleep(2)

driver.find_element(By.ID, "privacypolicy").click()
driver.find_element(By.ID, "termsconditions").click()

driver.find_element(By.ID, "search").click()
time.sleep(2)

driver.close()