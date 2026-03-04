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
    wait = WebDriverWait(driver,10)

    # find element
    search_ob = wait.until(EC.element_to_be_clickable((By.ID,'ucc-1')))
    search_ob.send_keys(query)
    search_ob.send_keys(Keys.ENTER)
    
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
    
        last_height = new_height
    results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'Nv2PK')))
    for r in results:
        print(r.text)
finally:
    driver.quit()