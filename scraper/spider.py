from selenium import webdriver
from selenium.webdriver.chrome.service import Service


targer_url = 'https://www.google.com/maps'
try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(targer_url)
finally:
    driver.quit()