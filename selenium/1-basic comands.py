

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)
driver.get("http://demo.automationtesting.in/Windows.html")
title = driver.title
print(title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.close() # zamyka tylko aktualnie zfocusowana
driver.quit() # zamyka wszystkie karty