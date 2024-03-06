
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

# mouse hover
# menu = driver.find_element("id","sub-menu")
# actions = ActionChains(driver)
# actions.move_to_element(menu)


# drag and drop
# source = driver.find_element("id","drag1")
# target = driver.find_element("id","div2")
# actions = ActionChains(driver)
# actions.drag_and_drop(source, target)


# #click
# element_to_click = driver.find_element("id","alert")
# target = driver.find_element("id","div2")
# #Create the object for Action Chains
# actions = ActionChains(driver)
# actions.click(element_to_click)

# double click
element_to_double_click = driver.find_element("id","double-click")
# Create the object for Action Chains
actions = ActionChains(driver)
actions.double_click(element_to_double_click)
actions.perform()
