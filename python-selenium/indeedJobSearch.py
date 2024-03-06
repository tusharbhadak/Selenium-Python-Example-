from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def indeedJobSearch():
    browser = webdriver.Chrome()
    browser.get("https://in.indeed.com/")
    browser.implicitly_wait(5)
    searchBar = browser.find_element("id", "text-input-what")
    searchBar.send_keys("game developer")
    searchBar.send_keys(Keys.ENTER)

    browser.implicitly_wait(5)

    search_result = browser.find_elements(By.XPATH, "//h2/a")
    browser.implicitly_wait(5)

    file = open("job_search.csv", "a")
    file.write("\n")

    for job_element in search_result:
        job_title = job_element.text
        job_link = job_element.get_attribute("href")
        file.write("%s | link: %s \n" %(job_title, job_link))

    browser.close()

if __name__ == "__main__":
    indeedJobSearch()