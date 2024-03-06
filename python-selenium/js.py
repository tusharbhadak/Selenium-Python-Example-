from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
# driver.get("https://pythonbasics.org")
# js = 'alert("Hello World")'
# driver.execute_script(js)

# driver.get("http://stackoverflow.com/questions/7794087/running-javascript-in-selenium-using-python")
# click = "document.getElementsByClassName('comment-user')[0].click()"
# driver.execute_script(click)

# driver.implicitly_wait(3)

# scroll = "window.scrollTo(0, document.body.scrollHeight)"
# driver.execute_script(scroll)

# driver.get("https://www.tutorialspoint.com/index.htm")
# s = driver.find_element(By.XPATH, "//*[text()='Library']")
# driver.execute_script("arguments[0].click();", s)
# print("Page title after click: " + driver.title)

# driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
# driver.find_element(By.NAME, "username").send_keys("Python")

# print(driver.execute_script('return document.getElementsByName("username")[0].value'))

driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
# driver.find_element(By.NAME, "spbutton").click()
# driver.execute_script("arguments[0].click();", btn)
print(driver.execute_script('return document.title'))
print(driver.execute_script('return document.url'))
driver.implicitly_wait(3)

driver.close()