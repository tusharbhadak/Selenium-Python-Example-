import os,time,logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

os.environ['WDM_PROGRESS_BAR'] = str(0)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument("--start-maximized")

driver = webdriver.Chrome()
driver.get("https://www.yahoo.com/")
time.sleep(10)
driver.find_element(By.XPATH, "//input[@name='p']").send_keys("educative.io")
time.sleep(10)
output_path = './'
driver.get_screenshot_as_file(os.path.join(output_path,'screenshot.png'))

auto_suggest_list_xpath = "//ul[@role='listbox']//li"
WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH, auto_suggest_list_xpath)))

elements = driver.find_elements(By.XPATH,"//ul[@role='listbox']//li")

print("Count of Auto Suggestion Elements = ",len(elements))
for ele in elements:
    print("<br>",ele.text)

driver.close()