#regionImport
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.BaseClass import BaseClass
from pageObjects.loginPage import LogInPage
from pageObjects.planPage import PlanPage
from pageObjects.storagePage import StoragePage
import time
#endregion

class Test_Login(BaseClass):

    def test_login(self):
        log = self.getLogger()
        time.sleep(5)
        logInPage = LogInPage(self.driver)
        logInPage.logIn()
        time.sleep(2)
        try:
            #assert self.driver.current_url == "http://localhost:28555/devices"
            log.info("User sucessfully logged")
        except:
            log.critical("LogIn Failed")
            raise

class Test_AddDevice(BaseClass):

    def test_Add_Device(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        logInPage = LogInPage(self.driver)
        logInPage.logIn()
        try:
            time.sleep(2)
            if self.driver.find_element(By.ID,"mat-badge-content-0").is_displayed():
                self.driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[2]/button[1]').click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-activate-devices-table/div/div[3]/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr/td[1]/mat-checkbox/label/span[1]').click()
                self.driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-activate-devices-table/div/div[4]/app-save-button/button/span[1]').click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,'//app-license[2]/p').click()
                self.driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-licenses-list/div/div[4]/app-save-button/button/span[1]/span').click()
                time.sleep(2)
                assert self.driver.find_element(By.ID,"mat-badge-content-0").is_displayed()==False
                log.error("Device was added successfully")
            else:
                log.info("There are no devices to activate")
        except:
                log.error("Device was not added")
                raise






