from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(0.5)

# website 1
# driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

# time.sleep(1)
# s = driver.find_element(By.XPATH, "//input[@type='file']")

# s.send_keys("C:/Users/gupta/Downloads/photopea.png")
# time.sleep(2)

# website 2
# driver.get("https://the-internet.herokuapp.com/upload")
# driver.find_element(By.ID, "file-upload").send_keys("C:/Users/gupta/Downloads/photopea.png")
# driver.find_element(By.ID, "file-submit").submit()

# time.sleep(2)

# if(driver.page_source.find("File Uploaded!")):
#     print("File upload success")
# else:
#     print("file upload not success")

# website 3

driver.get("http://autopract.com/selenium/upload1/")
file_input = driver.find_element(By.NAME, "files[]")
file_path = "C:/Users/gupta/Downloads/photopea.png"
file_input.send_keys(file_path)

time.sleep(2)

driver.find_element(By.CLASS_NAME, "start").click()

time.sleep(2)

print(driver.find_element(By.CLASS_NAME, "name").text)

driver.close()