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

class Test_Storages(BaseClass):

    def test_add_Local_Storage(self):
        
        self.driver.implicitly_wait(5)
        log = self.getLogger()
        logInPage = LogInPage(self.driver)
        logInPage.logIn()
        time.sleep(2)
        assert self.driver.current_url == "https://3be5838c-0e80-4f15-9003-3a1d5b749330.testing.xopero.com/devices"
  
        storagePage = StoragePage(self.driver)
        storagePage.storagePage()
        storagePage.AddStorage()
        storagePage.StorageName().clear()
        storagePage.StorageName().send_keys('Lokal')
        log.info("Name for local storage set as 'Lokal'")
        storagePage.LocalPath().send_keys('D:\\storage beta')
        storagePage.Save()

        self.driver.refresh()
        time.sleep(2)

        try:
            assert self.driver.find_element(By.XPATH,"//*[contains(text(),'Lokal')]").is_displayed()
            log.info("Local storage created")
        except:
            log.critical("Local storage creation failed")
            raise

    def test_add_SMB_Storage(self):

        self.driver.implicitly_wait(5)
        log = self.getLogger()

        time.sleep(2)
        storagePage = StoragePage(self.driver)
        storagePage.storagePage()
        storagePage.AddStorage()
        time.sleep(2)

        storagePage.StorageName().clear()
        storagePage.StorageName().send_keys('SMB')
        log.info("Name for SMB storage set as 'SMB'")
        storagePage.StorageTypeSelect()
        storagePage.Type_SMB()
        storagePage.SMBusername().send_keys('admin')
        storagePage.SelectPassword()

        log.info("Creating password for SMB")
        storagePage.AddNewPassword()
        storagePage.PasswordName().send_keys("Admin")
        passwords = storagePage.Passwords()
        for password in passwords:
            password.send_keys("Admin_123")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-passwords-form-container/app-passwords-form/form/div[3]/app-save-button/button/span[1]/span").click()
        time.sleep(2)
        log.info("Password for SMB storage set")


        storagePage.SMBpath().send_keys(r"\\192.168.0.198\Public\MStasiak")

        storagePage.Save()
        self.driver.refresh()
        time.sleep(2)
        try:
            assert self.driver.find_element(By.XPATH,"//*[contains(text(),'Lokal')]").is_displayed()
            log.info("SMB storage created")
        except:
            log.critical("SMB storage creation failed")
            raise

    def test_add_NFS_Storage(self):
        self.driver.implicitly_wait(5)
        log = self.getLogger()

        time.sleep(2)
        storagePage = StoragePage(self.driver)
        storagePage.storagePage()
        storagePage.AddStorage()
        time.sleep(2)

        storagePage.StorageName().clear()
        storagePage.StorageName().send_keys('NFS')
        log.info("Name for NFS storage set as 'NFS'")

        storagePage.StorageTypeSelect()
        storagePage.Type_NFS()
        storagePage.NFSpath().send_keys("192.168.0.198:/StorageNFS/Marek")
        storagePage.Save()

        self.driver.refresh()
        time.sleep(2)
        try:
            assert self.driver.find_element(By.XPATH,"//*[contains(text(),'NFS')]").is_displayed()
            log.info("NFS storage created")
        except:
            log.critical("NFS storage creation failed")
            raise

    def test_add_S3_Storage(self):
        self.driver.implicitly_wait(5)
        log = self.getLogger()

        time.sleep(2)
        storagePage = StoragePage(self.driver)
        storagePage.storagePage()
        storagePage.AddStorage()
        time.sleep(2)

        storagePage.StorageName().clear()
        storagePage.StorageName().send_keys('Minio S3')
        log.info("Name for S3 storage set as 'Minio S3'")


        storagePage.StorageTypeSelect()
        storagePage.S3()
        storagePage.LoginS3().send_keys("minioadmin")
        storagePage.SelectPassword()

        log.info("Creating password for MinioS3")
        storagePage.AddNewPassword()
        storagePage.PasswordName().send_keys("minio")
        passwords = storagePage.Passwords()
        for password in passwords:
            password.send_keys("minioadmin")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-passwords-form-container/app-passwords-form/form/div[3]/app-save-button/button/span[1]/span").click()
        time.sleep(2)
        log.info("Password for MinioS3 storage set")

        storagePage.S3Url().send_keys("http://192.168.4.237:9000")
        storagePage.S3Bucket().send_keys("storage")
        storagePage.Save()

        self.driver.refresh()
        time.sleep(2)
        try:
            assert self.driver.find_element(By.XPATH,"//*[contains(text(),'Minio S3')]").is_displayed()
            log.info("S3 storage created")
        except:
            log.critical("S3 storage creation failed")
            raise

    def test_add_BackBlaze_storage(self):
        self.driver.implicitly_wait(5)
        log = self.getLogger()              #
        logInPage = LogInPage(self.driver)  #
        logInPage.logIn()

        time.sleep(2)
        storagePage = StoragePage(self.driver)
        storagePage.storagePage()
        storagePage.AddStorage()
        time.sleep(2)

        storagePage.StorageName().clear()
        storagePage.StorageName().send_keys('BackBlaze')
        log.info("Name for Blackblaze storage set as 'Backblaze'")

        storagePage.StorageTypeSelect()
        storagePage.BackBlaze()
        storagePage.LoginS3().send_keys("0032ff820db6e990000000006")

        storagePage.SelectPassword()

        log.info("Creating password for BackBlaze")
        storagePage.AddNewPassword()
        storagePage.PasswordName().send_keys("Backblaze")
        passwords = storagePage.Passwords()
        for password in passwords:
            password.send_keys("K003XGuH9NSu9rTu/lSQ6kVcc8W1jEk")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-passwords-form-container/app-passwords-form/form/div[3]/app-save-button/button/span[1]/span").click()
        time.sleep(2)
        log.info("Password for BackBlaze storage set")

        dropdown = self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-backblaze/ng-select")
        dropdown.click()
        self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-backblaze/ng-select/ng-dropdown-panel/div[2]/div[2]/div[4]/div").click()
        log.info("Storage region set")

        storagePage.BackBlazeBucket().send_keys("Wuwuwu")
        time.sleep(1)
        storagePage.Save()

        self.driver.refresh()
        time.sleep(2)
        try:
            assert self.driver.find_element(By.XPATH,"//*[contains(text(),'BackBlaze')]").is_displayed()
            log.info("Backblaze storage created")
        except:
            log.critical("Backblaze storage creation failed")
            raise

    def test_xoperoStorage(self):
        storagePage = StoragePage(self.driver)
        log = self.getLogger()
        try: 
            
            self.driver.implicitly_wait(5)
            time.sleep(2)
            storagePage.storagePage()
            time.sleep(1)
            assert self.driver.find_element(By.XPATH,"//*[contains(text(),'Xopero Storage #1')]").is_displayed()
            log.info("Xopero storage is avaiable")
        except:
            log.critical("Xopero storage is not avaiable!")
            raise
        return