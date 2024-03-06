from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

time.sleep(2)

driver.find_element(By.NAME, "RESULT_TextField-1").send_keys("Harshit")
driver.find_element(By.NAME, "RESULT_TextField-2").send_keys("Gupta")
driver.find_element(By.NAME, "RESULT_TextField-3").send_keys("9898767876")
driver.find_element(By.NAME, "RESULT_TextField-4").send_keys("India")
driver.find_element(By.NAME, "RESULT_TextField-5").send_keys("Surat")
driver.find_element(By.NAME, "RESULT_TextField-6").send_keys("abc@gmail.com")

driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label").click()

driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[2]/td/label").click()
driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[5]/td/label").click()

timeToConnect = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))
timeToConnect.select_by_visible_text("Morning")

file_input = driver.find_element(By.NAME, "RESULT_FileUpload-10")
file_path = "C:/Users/gupta/Downloads/photopea.png"
file_input.send_keys(file_path)

time.sleep(5)

driver.find_element(By.NAME, "Submit").click()

time.sleep(10)

driver.close()