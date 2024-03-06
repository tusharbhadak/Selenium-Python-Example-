from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class instagramBot:
    def __init__(self, username, password):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.opts)

        self.username = username
        self.password = password

        self.driver.get("https://instagram.com")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(self.username)
        self.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(self.password)

        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Log in')]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

instagramBot("_imharshit._", "Sample Password")
