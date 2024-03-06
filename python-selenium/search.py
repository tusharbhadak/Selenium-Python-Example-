from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)

# search_bar = driver.find_element("id", "id-search-field")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.BACK_SPACE)
# time.sleep(3)
# print(driver.current_url)

# driver.close()
# print("Sample test case successfully completed")

assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()