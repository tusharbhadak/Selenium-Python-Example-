from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
# driver.fullscreen_window()
# driver.set_window_size(500,600) set window size
# driver.set_window_position(x=500, y=400) broswer position
# driver.set_window_rect(x=30, y=30, width=450, height=500)
# window_pos = driver.get_window_position()
# print(window_pos)

# print(driver.get_window_size())

driver.get("https://www.google.com/")
time.sleep(3)

driver.get("https://www.youtube.com/")
time.sleep(3)

driver.back() #to move back

driver.forward() #to move forward

driver.close()