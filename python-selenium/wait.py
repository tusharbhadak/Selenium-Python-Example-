from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
# driver.implicitly_wait(10)

driver.get("https://intellipaat.com/")

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.LINK_TEXT, "Courses"))
# )

# element.click()

timeout = 10
try:
    wait = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Explore Courses"))
    )

    # wait.click()
    print("Element is visible and clicked!")
except TimeoutException:
    print("Timed out waiting or element to be visible")
finally:
    driver.quit()