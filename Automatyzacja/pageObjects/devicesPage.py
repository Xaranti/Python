from selenium.webdriver.common.by import By

class DevicePage:

    device = (By.XPATH,"/html/body/app-root/app-main/app-menu/section/nav[1]/a[1]")
    assingPlan = (By.XPATH,"//*[contains(text(),'Assign plan')]")
    mainRestore = (By.XPATH,"//*[contains(text(),'Main')]/../../footer/button[1]")
    availablePlans = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/ng-select")
    restoreLast = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/div/app-browser-container/app-browser/div/div/app-browser-backups/div/div/div[2]/div/button")
    restore_as_iscis = (By.XPATH,"//*[contains(text(),'iSCSI target')]")
    restoreAll = (By.XPATH,"//*[contains(text(),'Restore all')]")
    fileImage = (By.XPATH,"//*[contains(text(),'file image')]")
    restoreSelected = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-data-to-restore/div/div[4]/button")
    fistDisk = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-data-to-restore/div/div[3]/div/app-hdd/div/div/div/div[1]/div/mat-checkbox")
    selectDirectory = (By.XPATH,"//*[contains(text(),'Select directory')]")
    startNow = (By.XPATH,"//*[contains(text(),'Start now')]")
    imageFormat = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[3]/app-aside/ng-component/app-new-restore/div/app-restore-hdd-container/app-restore-hdd/div/div[1]/app-disk-image-options/div/div[2]/ng-select/div")
    BMR = (By.XPATH,"//*[contains(text(),'BMR')]")


    def __init__(self,driver):
        self.driver = driver

    def devicePage(self):
        self.driver.find_element(*DevicePage.device).click()

    def AssignPlan(self):
        self.driver.find_element(*DevicePage.assingPlan).click()

    def mainDeviceRestore(self):
        self.driver.find_element(*DevicePage.mainRestore).click()

    def PlanList(self):
        self.driver.find_element(*DevicePage.availablePlans).click()

    def RestoreLast(self):
        self.driver.find_element(*DevicePage.restoreLast).click()

    def as_ISCSI(self):
        self.driver.find_element(*DevicePage.restore_as_iscis).click()

    def RestoreAll(self):
        self.driver.find_element(*DevicePage.restoreAll).click()

    def FileImage(self):
        self.driver.find_element(*DevicePage.fileImage).click()

    def RestoreSelected(self):
        self.driver.find_element(*DevicePage.restoreSelected).click()

    def FirstDisk(self):
        self.driver.find_element(*DevicePage.fistDisk).click()

    def SelectDirectory(self):
        self.driver.find_element(*DevicePage.selectDirectory).click()

    def StartNow(self):
        self.driver.find_element(*DevicePage.startNow).click()

    def ImageFormat(self):
        self.driver.find_element(*DevicePage.imageFormat).click()

    def BareMetalRestore(self):
        self.driver.find_element(*DevicePage.BMR).click()