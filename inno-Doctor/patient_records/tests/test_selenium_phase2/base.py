from selenium import webdriver
from config import Configuration
class Baseconfig:
    driver = webdriver.Chrome(Configuration.CHROME_PATH)
    # driver.get(Configuration.BASE_URL)