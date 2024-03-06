from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bandcamp.com/")

#to play song
# driver.find_element(By.CLASS_NAME, "play-btn").click() 

# genereList = driver.find_elements(By.CLASS_NAME, "discover-item")
# print(len(genereList))

driver.find_element("name", "q").send_keys("metal", Keys.ENTER)

driver.find_element(By.LINK_TEXT, "Metal Blade Records").click()

# driver.find_element(By.CLASS_NAME, "title").click()
listOfElements = driver.find_elements(By.CLASS_NAME, "title")
print(listOfElements)

#driver.find_element(By.CLASS_NAME, "playbutton").click()

time.sleep(2)

driver.close()