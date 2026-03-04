from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
query = os.getenv('SEARCH_QUERY')
TARGET_URL = 'https://www.google.com/maps'
try:
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(TARGET_URL)
    print(f'Page title:{driver.title}')
    wait = WebDriverWait(driver,10)

    # find element
    search_ob = wait.until(EC.element_to_be_clickable((By.ID,'ucc-1')))
    search_ob.send_keys(query)
    sleep(2)
    search_ob.send_keys(Keys.ENTER)
    sleep(2)

finally:
    driver.quit()