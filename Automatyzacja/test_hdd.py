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
from pageObjects.devicesPage import DevicePage
import time
import socket
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
#endregion

class Test_HDD(BaseClass):

    def test_addPlan(self):

        log = self.getLogger()
        self.driver.implicitly_wait(5)

        logInPage = LogInPage(self.driver)
        logInPage.logIn()
        time.sleep(2)
        #assert self.driver.current_url == "http://localhost:28555/devices"

        planPage = PlanPage(self.driver)
        planPage.planPage()
        time.sleep(2)
        #assert self.driver.current_url == "http://localhost:28555/plans/backup"

        try:

            if self.driver.find_element(By.XPATH,"//*[text()='Backup HDD']").is_displayed():
                log.warning("Plan 'Backup HDD' already exist")
                planRow = self.driver.find_element(By.XPATH,"//*[text()='Backup HDD']/../..")
                planPage.RunPlan(planRow)
                planPage.RunIncremental(planRow)
                log.info("Plan 'Backup HDD' started as incremental backup")
                planPage.ClosePlanDashboard()

            else:
                pass

        except:

                planPage.AddPlan()
                planPage.PlanName().clear()
                planPage.PlanName().send_keys("Backup HDD")
                log.info("Plan name set as 'Backup HDD' ")
                planPage.HowToProtect()
                planPage.ImageLevel()
                planPage.WhichDevices()
                main = self.driver.find_element(By.XPATH,"//span[text()='Main']/../../..")
                planPage.MainDeviceCheckbox(main)
                log.info("Main device choosen")
                planPage.ApplyButton()
                planPage.WhatToProtect()
                planPage.DeviceName()

                try:

                    diskLetter = self.driver.find_element(By.XPATH,"//*[contains(text(),'(G:)')]/../../../..")
                    planPage.DiskCheckBox(diskLetter)
                    log.info("Disk 'G:' set for backup")
                    planPage.SaveChoice()
                    planPage.ApplyButton()
                    planPage.WhereToStore()
                    time.sleep(1)
                    planPage.XoperoStorage()
                    time.sleep(1)
                    log.info("Storage for HDD backup set as Xopero Storage")
                    planPage.When()
                    planPage.StartAt().send_keys('1111')
                    planPage.Next()
                    planPage.SaveSchedule()
                    log.info("Schedule set for 11:11")
                    time.sleep(1)
                    planPage.SaveRun()
                    log.info("Plan 'Backup HDD' started succesfully")

                except:
                    
                    log.error("Creating plan Failed")
                    raise
    
    def test_systemDisk(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        planPage = PlanPage(self.driver)
        #planPage.planPage()

        try:

            if self.driver.find_element(By.XPATH,"//*[text()='System Disk Backup']").is_displayed():
                log.warning("Plan 'System Disk Backup' already exist")
                planRow = self.driver.find_element(By.XPATH,"//*[text()='System Disk Backup']/../..")
                planPage.RunPlan(planRow)
                planPage.RunIncremental(planRow)
                log.info("Plan 'System Disk Backup' started as incremental backup")
                planPage.ClosePlanDashboard()

            else:
                pass

        except:

                planPage.AddPlan()
                planPage.PlanName().clear()
                planPage.PlanName().send_keys("System Disk Backup")
                log.info("Plan name set as 'System Disk Backup' ")
                planPage.HowToProtect()
                planPage.ImageLevel()
                planPage.WhichDevices()
                main = self.driver.find_element(By.XPATH,"//span[text()='Main']/../../..")
                planPage.MainDeviceCheckbox(main)
                log.info("Main device choosen")
                planPage.ApplyButton()
                planPage.WhatToProtect()
                planPage.DeviceName()

                try:

                    diskLetter = self.driver.find_element(By.XPATH,"//*[contains(text(),'(C:)')]/../../../..")
                    planPage.DiskCheckBox(diskLetter)
                    log.info("Disk 'C:' set for backup")
                    planPage.SaveChoice()
                    planPage.ApplyButton()
                    planPage.WhereToStore()
                    planPage.XoperoStorage()
                    log.info("Storage for HDD backup set as Xopero Storage")
                    planPage.When()
                    planPage.StartAt().send_keys('1111')
                    planPage.Next()
                    planPage.SaveSchedule()
                    log.info("Schedule set for 11:11")
                    time.sleep(2)
                    planPage.SaveRun()
                    time.sleep(1)
                    log.info("Plan 'System Disk Backup' started succesfully")

                except:
                    
                    log.error("Creating plan Failed")
                    raise

    def test_Xopero_Disk_Variable(self):

        log = self.getLogger()
        self.driver.implicitly_wait(5)
        planPage = PlanPage(self.driver)
        #planPage.planPage()


        try:

            if self.driver.find_element(By.XPATH,"//*[text()='Xopero Var Backup']").is_displayed():
                log.warning("Plan 'System Disk Backup' already exist")
                planRow = self.driver.find_element(By.XPATH,"//*[text()='System Disk Backup']/../..")
                planPage.RunPlan(planRow)
                planPage.RunIncremental(planRow)
                log.info("Plan 'Xopero Var Backup' started as incremental backup")
                planPage.ClosePlanDashboard()

            else:
                pass
        except:

            planPage.AddPlan()
            planPage.PlanName().clear()
            planPage.PlanName().send_keys("Xopero Var Backup")
            log.info("Plan name set as 'Xopero Var Backup' ")
            planPage.HowToProtect()
            planPage.ImageLevel()
            planPage.WhichDevices()
            main = self.driver.find_element(By.XPATH,"//span[text()='Main']/../../..")
            planPage.MainDeviceCheckbox(main)
            log.info("Main device choosen")
            planPage.ApplyButton()
            planPage.WhatToProtect()
            planPage.DeviceName()

            try:
                self.driver.find_element(By.CSS_SELECTOR,"div[class='item__content']").click()
                self.driver.find_element(By.XPATH,"//*[contains(text(),'Set global rules')]").click()
                self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-add-rule/div/div[3]/div/div[2]/app-rule/div/app-paths/div/form/ng-select").click()
                self.driver.find_element(By.XPATH, "//*[contains(text(),'SYSTEM_DISK')]").click()
                planPage.ApplyButton()
                planPage.WhereToStore()
                time.sleep(1)
                planPage.XoperoStorage()
                time.sleep(1)
                log.info("Storage for HDD backup set as Xopero Storage")
                planPage.When()
                planPage.StartAt().send_keys('1111')
                planPage.Next()
                planPage.SaveSchedule()
                log.info("Schedule set for 11:11")
                time.sleep(2)
                planPage.SaveRun()
                time.sleep(1)

                log.info("Plan 'System Disk Backup' started succesfully")

            except:
            
                log.error("Creating plan Failed")
                raise

    def test_prePlan(self):

        log = self.getLogger()
        self.driver.implicitly_wait(5)
        devicePage = DevicePage(self.driver)
        devicePage.devicePage()
        planPage = PlanPage(self.driver)
        
        time.sleep(1)
        devicePage.AssignPlan()
        self.driver.find_element(By.XPATH,'//*[contains(text(),"Endpoint&Server Total Protection")]').click()

        time.sleep(1)
        #assert self.driver.find_element(By.XPATH,"//*[text()='Endpoint&Server Total Protection']").is_displayed()
        log.info("Predefined plan was successfuly added to device")

        planPage.planPage()
        time.sleep(2)
        try:
            if self.driver.find_element(By.XPATH,"//*[text()='Endpoint&Server Total Protection']").is_displayed():
                    log.warning("Plan 'System Disk Backup' already exist")
                    planRow = self.driver.find_element(By.XPATH,"//*[contains(text(),'Endpoint&Server Total Protection')]/../..")
                    planPage.RunPlan(planRow)
                    planPage.RunFull(planRow)
                    log.info("Plan 'Endpoint&Server Total Protection' started as Full backup")
                    planPage.ClosePlanDashboard()
        except:
            log.error("Error during runnin predefined plan")
            raise

    def test_restoreISCSI(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        devicePage = DevicePage(self.driver)
        devicePage.devicePage()
        time.sleep(1)
        devicePage.mainDeviceRestore()
        time.sleep(1)
        #devicePage.PlanList()
        #
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        planlist = WebDriverWait(self.driver, 10,ignored_exceptions=ignored_exceptions)\
                        .until(EC.presence_of_element_located((devicePage.availablePlans)),log.error("Plan list not found"))

        try:
            self.driver.find_element(By.XPATH,"//*[contains(text(),'Backup HDD')]").click()
            try:
                devicePage.RestoreLast()
                devicePage.as_ISCSI()
                devicePage.RestoreAll()

                hostname = socket.gethostname()
                #ip = socket.gethostbyname(hostname)
                ip = '192.168.4.237'

                ethernet = self.driver.find_element(By.XPATH,"//h4[contains(text(),'Ethernet')]/..")
                ipPanel = ethernet.find_element(By.CSS_SELECTOR,"p[class='ng-star-inserted']").text
                assert ipPanel in ip

                self.driver.find_element(By.XPATH,"//*[contains(text(),'Run iSCSI')]").click()
                log.info("Uruchomiono restore poprzez iSCSI")

            except:
                log.error("Error during starting restore plan")
                raise
        except:
            log.error("Did not find indicated plan to restore")
            raise

    def test_restore_file_image(self,getData):

        log = self.getLogger()
        self.driver.implicitly_wait(5)

        self.driver.refresh()
        devicePage = DevicePage(self.driver)
        devicePage.devicePage()

        devicePage.mainDeviceRestore()
        #devicePage.PlanList()
        #
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        planlist = WebDriverWait(self.driver, 10,ignored_exceptions=ignored_exceptions)\
                        .until(EC.presence_of_element_located((devicePage.availablePlans)),log.error("Plan list not found"))

        planlist.click()
        #
        try:
            self.driver.find_element(By.XPATH,"//*[contains(text(),'Backup HDD')]").click()
            log.info("Restore Plan choosen")
            try:
                devicePage.RestoreLast()
                devicePage.FileImage()
                devicePage.FirstDisk()
                devicePage.RestoreSelected()

                devicePage.ImageFormat()
                formats = self.driver.find_elements(By.CSS_SELECTOR,"div[role='option']")
                for format in formats:
                    if format.text == getData["type"]:
                        log.info("Restore set as %s" %(getData["type"]))
                        format.click()
                        break

                devicePage.SelectDirectory()

                self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]/app-aside/ng-component/app-browse-device-files/div/div[3]/app-files-browser/app-files/ul/li[2]/div/app-icon").click()
                folderTree = self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]/app-aside/ng-component/app-browse-device-files/div/div[3]/app-files-browser/app-files/ul/li[2]")
                mainTree = self.driver.find_elements(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]/app-aside/ng-component/app-browse-device-files/div/div[3]/app-files-browser/app-files/ul/li[2]/ul/li")

                #iteration through folders + avoidin stale element reference
                for i in range(1,len(mainTree)):
                    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
                    element = WebDriverWait(self.driver, 5,ignored_exceptions=ignored_exceptions)\
                        .until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-main/div/app-content/div[1]/aside[4]/app-aside/ng-component/app-browse-device-files/div/div[3]/app-files-browser/app-files/ul/li[2]/ul/li[%i]"%(i))))
                    if element.text == 'Backup HDD':                       
                         log.info("Folder already exist, starting restore")
                         element.find_element(By.TAG_NAME,'mat-checkbox').click()
                         self.driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()
                         time.sleep(1)
                         devicePage.StartNow()
                         log.info("Restore started successfuly")
                         return
                    else:
                        pass


                time.sleep(1)
                log.info("Restore folder not found, creating new one")
                x = self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]/app-aside/ng-component/app-browse-device-files/div/div[3]/app-files-browser/app-files/ul/li[2]/div")
                x.find_element(By.CSS_SELECTOR,"svg[data-icon='folder-plus']").click()
                folderTree.find_element(By.CSS_SELECTOR,"input[data-placeholder='New catalog name']").send_keys('Backup HDD')
                folderTree.find_element(By.CSS_SELECTOR,"button[title='Add catalog']").click()
                log.info("Restore folder created")
                time.sleep(1)
                self.driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,"//*[contains(text(),'Start now')]").click()
                log.info("Restore started sucessfuly")

            except:
                log.error('Error during lunching restore')
                raise
        except:
            log.warning('Intended plan not found')
            raise


    @pytest.fixture(params= [{'type':'RAW','plan':'Backup HDD'},{'type':'VHD','plan':'Backup HDD'},{'type':'VHDX','plan':'Backup HDD'},{'type':'VMDK','plan':'Backup HDD'}])
    def getData(self, request):
        return request.param

    def test_restoreBMR(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        logInPage = LogInPage(self.driver)
        devicePage = DevicePage(self.driver)
        planPage = PlanPage(self.driver)
        log.info('BMR restore started')
        logInPage.logIn()
        time.sleep(1)
        devicePage.devicePage()

        devicePage.mainDeviceRestore()
        log.info("Main device set to restore")
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        planlist = WebDriverWait(self.driver, 10,ignored_exceptions=ignored_exceptions)\
                        .until(EC.presence_of_element_located((devicePage.availablePlans)),log.error("Plan list not found"))
        planlist.click()

        assert self.driver.find_element(By.XPATH,"//*[contains(text(),'Backup HDD')]").is_displayed()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'Backup HDD')]").click()
        log.info("Restore Plan choosen")
        devicePage.RestoreLast()
        devicePage.BareMetalRestore()
        log.info("Restore type set as BMR")
        devicePage.FirstDisk()
        devicePage.RestoreSelected()
        devicePage.SelectDirectory()
        BrowseDevices = self.driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[4]")

        diskLetter = BrowseDevices.find_element(By.XPATH,"//*[contains(text(),'(G:)')]/../../../..")
        #time.sleep(1)
        diskCheckbox = WebDriverWait(diskLetter,10)\
                          .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"label[class='mat-checkbox-layout']")))
        diskCheckbox.click()
        #self.driver.execute_script("arguments[0].click();",diskLetter.find_element(By.CSS_SELECTOR,"label[class='mat-checkbox-layout']"))
        time.sleep(5)
        log.info("Directory to restore set")
        