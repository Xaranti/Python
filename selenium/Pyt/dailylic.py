from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
    
    
PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)
driver.get("http://localhost:28555/")
driver.maximize_window()
time.sleep(2)
log = driver.find_element_by_name('login')
log.send_keys('admin@xopero.com')

pas = driver.find_element_by_id('mat-input-1')
pas.send_keys('Admin_123')

driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/app-auth/div/app-auth-login/div/form/app-save-button/button').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[2]/a').click()
driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside[1]/app-aside/ng-component/app-settings/div/div[3]/div[1]').click()
driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-license-package/div/div[3]/div[2]').click()
#gitprot = driver.find_element_by_xpath("//*[contains(text(),'GitProtect')]")
#print(gitprot.is_displayed())

licencje = ['Microsoft 365','GitProtect','Feature worker','Server Agent','zmyslona']
for lic in licencje:
    try:
        istrue = driver.find_element_by_xpath("//*[contains(text(),'%s')]" %(lic)).is_displayed()
        print("Dostępność licencji %s = " % (lic),istrue)
    except:
        print("Dostępność licencji %s = " % (lic),"False")