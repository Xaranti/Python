from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path(sciezka))
driver.get("http://youtube.com/") #FR
time.sleep(5)
print(driver.title)
driver.get("https://www.google.com/") #TT
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)