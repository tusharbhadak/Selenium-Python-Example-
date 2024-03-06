from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

print("parent: " ,driver.current_window_handle)

print(driver.window_handles)

driver.find_element(By.LINK_TEXT, "Window Popup Modal").click()
print("child: " ,driver.window_handles[0])

driver.find_element(By.LINK_TEXT, "Follow On Twitter").click()
print("twitter: " ,driver.window_handles[1])
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Like us On Facebook").click()
print("facebook: " ,driver.window_handles[2])
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Follow us On Linkedin").click()
print("linkedin: " ,driver.window_handles[3])
time.sleep(2)

twitter = driver.window_handles[1]
time.sleep(3)
driver.switch_to.window(twitter)
time.sleep(3)

handles = driver.window_handles
for i in handles:
    driver.switch_to.window(i)

    print(driver.title)
    print(driver.current_window_handle)


driver.close()