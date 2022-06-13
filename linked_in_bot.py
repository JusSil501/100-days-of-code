import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import common
import os
from dotenv import load_dotenv
import time
load_dotenv("/Users/justinsilva/Documents/Environ_variables/.env")
chrome_driver_path = "/Users/justinsilva/100 days of Code Projects/chromedriver"

def save_job_listing():
    # right_rail = driver.find_elements(By.CSS_SELECTOR, ".jobs-search__right-rail .relative")

    all_jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
    for job in all_jobs:
        job.click()
        time.sleep(2)
        save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save.click()
        time.sleep(2)
        ex = driver.find_element(By.CSS_SELECTOR, "li-icon.artdeco-button__icon svg.mercado-match")
        ex.click()



driver = webdriver.Chrome(executable_path=chrome_driver_path)



url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

response = driver.get(url)
def sign_in():
    sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
    sign_in.click()

    username = driver.find_element(By.ID, "username")
    username.send_keys("jgesmarsilva@gmail.com")

    username = driver.find_element(By.ID, "password")

    username.send_keys(os.environ.get('PASSWORD'))

    final_sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    final_sign_in.click()

sign_in()
time.sleep(4)
save_job_listing()
