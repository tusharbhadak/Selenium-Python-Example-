from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pynishant.github.io/dropdown-selenium-python-select.html")

# using action chain
# myOption = driver.find_element(By.XPATH, "//select[@multiple]/option[contains(text(), 'C#')]")
# myOption1 = driver.find_element(By.XPATH, "//select[@multiple]/option[contains(text(), 'PHP')]")
# myOption2 = driver.find_element(By.XPATH, "//select[@multiple]/option[contains(text(), 'Java')]")

# ActionChains(driver).key_down(Keys.CONTROL).click(myOption).key_up(Keys.CONTROL).perform()
# ActionChains(driver).key_down(Keys.CONTROL).click(myOption1).key_up(Keys.CONTROL).perform()
# ActionChains(driver).key_down(Keys.CONTROL).click(myOption2).key_up(Keys.CONTROL).perform()

dropdown = Select(driver.find_element("id","lang2"))
dropdown.select_by_visible_text("Python")
dropdown.select_by_index(1)
dropdown.select_by_value("php")

time.sleep(1)

dropdown.deselect_by_value("php")

time.sleep(2)


driver.close()