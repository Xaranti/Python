from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element_by_css_selector('.uitk-tab:nth-child(2) .uitk-icon').click()
driver.find_element_by_css_selector('.uitk-layout-grid-item:nth-child(1) > div > .uitk-typeahead .uitk-faux-input').click()

