from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path(sciezka))

driver.get("http://demo.guru99.com/test/newtours/")
user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #return true/false based on element status
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed()) #return true/false based on element status
print(pwd_ele.is_enabled())

user_ele.send_keys('asd')
pwd_ele.send_keys('asd')
driver.find_element_by_name("submit").click()

driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("is round trip selected: ",roundtrip_radio.is_selected())
oneway_radio=driver.find_element_by_css_selector("input[value=oneway]")
print("is oneway trip selected: ",oneway_radio.is_selected())
time.sleep(3)
driver.close()
print("kurwa miszcz")


