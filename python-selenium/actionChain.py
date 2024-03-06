from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver.get("https://www.browserstack.com/")
driver.get("https://www.geeksforgeeks.org/")
# driver.get("https://internshala.com/")

driver.refresh()

# element = driver.find_element("link text", "Sign in")
# element = driver.find_element("link text", "Data Science")
# element = driver.find_element("link text", "Hire Talent")
# source_element = driver.find_element("link text", "Python")
# time.sleep(3)
# target_element = driver.find_element("link text", "Data Science & ML")
# time.sleep(3)

element = driver.find_element("link text", "Python")

action = ActionChains(driver)

action.click(on_element= element)
# action.click_and_hold(on_element= element)
# action.double_click(on_element= element)
# action.drag_and_drop(source_element, target_element)

# action.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()
# driver.close()

action.pause(5000)

action.click(on_element= element)

action.perform()