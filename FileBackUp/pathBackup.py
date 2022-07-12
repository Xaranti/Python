from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

def pathBackup(driver,planName,backupPath):
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'Plans')]").click()
    except:
        pass
    driver.find_element(By.XPATH,"//*[contains(text(),'Add plan')]").click()

    driver.find_element(By.NAME,"backupPlanName").clear()
    driver.find_element(By.NAME,"backupPlanName").send_keys("%s" %(planName))

    driver.find_element(By.XPATH,"//*[contains(text(),'How to protect')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'File-level')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'Which devices?')]").click()

    mainDevice = driver.find_element(By.XPATH,"//span[text()='Main']/../../..")
    mainDevice.find_element(By.CLASS_NAME, "mat-checkbox").click()

    driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'What to protect?')]").click()


    selectItems = driver.find_element(By.XPATH,"//div[text()='Select items to back up using']/..")
    selectItems.find_element(By.CSS_SELECTOR,"div[role='combobox']").click()
    selectItems.find_element(By.XPATH,"//*[contains(text(),'Set global rules')]").click()
    driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='path']").send_keys(backupPath)
    #driver.find_element(By.CSS_SELECTOR,"svg[data-icon='check']").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()

    driver.find_element(By.XPATH,"//*[contains(text(),'Where to store?')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[contains(text(),'Xopero Storage')]").click()

    driver.find_element(By.XPATH,"//*[contains(text(),'When?')]").click()
    startAt = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-add-schedule/form/div[3]/div/mat-accordion/mat-expansion-panel[1]/div/div/app-monthly/div/mat-radio-group/div/div[2]/app-time/mat-form-field/div/div[1]/div/input')
    startAt.send_keys('1111')
    driver.find_element(By.XPATH,"//*[contains(text(),'Next')]").click()
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    driver.find_element(By.XPATH,"//*[contains(text(),'Save&Run')]").click()



