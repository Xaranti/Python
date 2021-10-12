from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(5) #in seconds
assert "Welcome: Mercury Tours" in driver.title


driver.find_element_by_name('userName').send_keys('mercury')
driver.find_element_by_name('password').send_keys('mercury')

driver.find_element_by_name('submit').click()