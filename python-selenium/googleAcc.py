from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://mail.google.com/")

email_input = driver.find_element(By.NAME, "identifier")
email_input.send_keys("guptahoney081@gmail.com")
email_input.send_keys(Keys.ENTER)

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

password_input.send_keys("your_Password")
password_input.sendKeys(Keys.RETURN)

driver.close()