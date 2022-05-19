from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.action_chains import ActionChains
import time

def FileRestore_Cloud(driver,storage,backupName):
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH,'/html/body/app-root/app-main/app-menu/section/nav[1]/a[6]/span[2]').click()

    time.sleep(3)
    location = driver.find_element(By.XPATH,"//*[contains(text(),'%s')]" %(storage)) ##<--- wstaw nazwę magazynu, z którego chcesz przywracać
    parentLocation1 = location.find_element(By.XPATH,'./../..')
    parentLocation1.find_element(By.CLASS_NAME, "mat-button-wrapper").click()

    driver.find_element(By.XPATH,"//*[contains(text(),'Select resource')]").click()
    driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-select-worker/div/div[2]/app-filters-table/button').click()
    x = driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-select-worker/div/div[2]/app-filters-table/form/div/app-filters/app-filter-input/input')
    x.send_keys('STASIAK-M')

    time.sleep(2)
    driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-select-worker/div/div[3]/div/div/div/div").click()
    time.sleep(1)

    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'View available plans')]").is_displayed()
        driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/ng-select").click()
        driver.find_element(By.XPATH,"//*[contains(text(),'%s')]" %(backupName)).click()
    except:
        pass

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/div[2]/app-browser-container/app-browser/div/div/app-browser-backups/div/div/div[2]/div/button/span[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[contains(text(),'Restore all')]").click()
    time.sleep(1)

    driver.find_element(By.XPATH,"//*[contains(text(),'Select directory')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'New directory')]").click()    

    driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]/app-aside/ng-component/app-browse-device-files/div/div[3]/app-files-browser/app-files/ul/li[2]/div/app-icon").click()

    folderTree = driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]")
    restorePath = R"backup\Cloud" ##<--- wstaw ścieżkę backupu
    restorePath=restorePath.replace(":","")
    backupPath = restorePath.split("\\")
    fileName = backupPath.pop(-1)

    for folder in backupPath:
        time.sleep(1)
        folderTree.find_element(By.XPATH,"//span[text()='%s']/../../app-icon/fa-icon" %(folder)).click()
        #folderName.find_element(By.XPATH,"//*/app-icon").click()

    fileNameElem = folderTree.find_element(By.XPATH,"//span[text()='%s']" %(fileName))
    time.sleep(1)
    driver.find_element(locate_with(By.CSS_SELECTOR,  "label[class='mat-checkbox-layout']").to_left_of(fileNameElem)).click()


    driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'Start now')]").click()
    print("Test 1 - Uruchomienie FB restore z CLD: Pass")

    return()