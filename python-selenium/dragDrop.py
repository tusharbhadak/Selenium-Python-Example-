from selenium import webdriver
import time

driver  = webdriver.Chrome()

# Navigate to page stored as local file

driver.get("C:/Users/gupta/Downloads/python-selenium/index.html")
# Locate 'drag' element as source

circle1 = driver.find_element("id","drag")
time.sleep(3)

# Locate 'drop' element as target

circle2 = driver.find_element("id","drop")
time.sleep(3)

x_off = circle2.location.get("x")
y_off = circle2.location.get("y")

# Perform drag and drop action from

webdriver.ActionChains(driver).drag_and_drop_by_offset(circle1, x_off, y_off).perform()