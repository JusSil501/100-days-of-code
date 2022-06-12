from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
webdriver_path = "/Users/justinsilva/100 days of Code Projects/chromedriver"

driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
button = driver.find_element(By.ID, "bigCookie")
def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key

def check_cookies():
    cookies = (driver.find_element(By.ID, "cookies")).text
    actual_cookies = cookies.split()[0]
    try:
        return int(actual_cookies)
    except ValueError:
        return int((actual_cookies).replace(",", ""))



def check_upgrades():
    try:
        buy_upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
        for upgrades in buy_upgrades:
            upgrades.click()
    except selenium.common.exceptions.NoSuchElementException:
        return
def check_panels():
    buy = driver.find_element(By.XPATH, '//*[@id="storeBulkBuy"]')
    power_cost = {}
    try:

        buy_power = driver.find_elements(By.CSS_SELECTOR, "#products .enabled ")
        for key, power in enumerate(buy_power):
            print(key)
            print(power.get_property("id"))
            try:
                power_cost[power] = int((driver.find_element(By.CSS_SELECTOR, f".enabled .content #productPrice{key}")).text)
                print(power_cost[power])
            except ValueError:
                power_cost[power] = int((
                    (driver.find_element(By.CSS_SELECTOR, f".enabled .content #productPrice{key}")).text).replace(",", ""))
        values = list(power_cost.values())

        for power in buy_power:
            if check_cookies() > power_cost[power]:
                for i in range(len(values)-1, -1, -1):
                    if check_cookies() > values[i]:
                        get_key(values[i], power_cost).click()
                        buy.click()
    except selenium.common.exceptions.NoSuchElementException:
        return

start = time.time()

while True:
    try:
        while time.time() - start < 10:
            button.click()
        check_upgrades()
        check_panels()
        start = time.time()
    except ElementClickInterceptedException:
        pass




