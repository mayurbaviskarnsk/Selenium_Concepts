# Browser Commands
# Navigation Commands
# WebElement Commands
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.naukri.com/nlogin/login"
driver = webdriver.Chrome()

driver.get(url)
time.sleep(20)
driver.find_element(By.XPATH,'//*[@id="usernameField"]').send_keys("12345")