from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


TARGET_URL = 'https://www.google.com/maps'
try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(TARGET_URL)
    print(f'Page title:{driver.title}')
    wait = WebDriverWait(driver,10)

    # find element
    search_ob = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'UGojuc')))
    search_ob.send_keys('dentist Texas')
    search_ob.send_keys(Keys.ENTER)
    
finally:
    driver.quit()