from selenium import webdriver
from Screenshot import Screenshot as ss

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/c/c_for_loop.php")

page = ss.Screenshot("w3C.png")
# page.screenshot("w3.png")

# driver.save_screenshot("youtube.png")