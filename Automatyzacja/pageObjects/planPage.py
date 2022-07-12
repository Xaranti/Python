from selenium.webdriver.common.by import By


class PlanPage:

    plans = (By.XPATH,"//*[contains(text(),'Plans')]")
    addPlan = (By.XPATH,"//*[contains(text(),'Add plan')]")
    planName = (By.NAME,"backupPlanName")
    runPlan = (By.CSS_SELECTOR,"button[aria-label='button']")
    runFull = (By.XPATH,"//div[@class='cdk-overlay-pane']/div/div/button[2]")
    runIncremental = (By.XPATH,"//div[@class='cdk-overlay-pane']/div/div/button[3]")
    closePlanDashboard = (By.CSS_SELECTOR,"button[aria-label='Close']")
    howToProtect = (By.XPATH,"//*[contains(text(),'How to protect')]")
    fileLevel = (By.XPATH,"//*[contains(text(),'File-level')]")
    imageLevel = (By.XPATH,"//*[contains(text(),'Image-level')]")
    whichDevices = (By.XPATH,"//*[contains(text(),'Which devices?')]")
    mainDeviceCheckbox = (By.CLASS_NAME, "mat-checkbox")
    applyButton = (By.XPATH,"//*[contains(text(),'Apply')]")
    whatToProtect = (By.XPATH,"//*[contains(text(),'What to protect?')]")
    deviceName =  (By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-add-rule/div/div[3]/div[2]/div[2]/div/h3')
    diskCheckbox = (By.CSS_SELECTOR,"label[class='mat-checkbox-layout']")
    saveChoice = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[3]/app-aside/ng-component/app-add-device-rule/div/div[3]/button/span[1]")
    whereToStore = (By.XPATH,"//*[contains(text(),'Where to store?')]")
    xoperoStorage = (By.XPATH,"//*[contains(text(),'Xopero Storage')]")
    when = (By.XPATH,"//*[contains(text(),'When?')]")
    startAt = (By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-add-schedule/form/div[3]/div/mat-accordion/mat-expansion-panel[1]/div/div/app-monthly/div/mat-radio-group/div/div[2]/app-time/mat-form-field/div/div[1]/div/input')
    saveRun = (By.XPATH,"//*[contains(text(),'Save&Run')]")
    next = (By.XPATH,"//*[contains(text(),'Next')]")
    saveSchedule = (By.XPATH,"//button[@type='submit']")


    def __init__(self,driver):
        self.driver = driver

    def planPage(self):
        return self.driver.find_element(*PlanPage.plans).click()

    def AddPlan(self):
        return self.driver.find_element(*PlanPage.addPlan).click()

    def PlanName(self):
        return self.driver.find_element(*PlanPage.planName)

    def RunPlan(self,planRow):
        return planRow.find_element(*PlanPage.runPlan).click()

    def RunFull(self,planRow):
        return planRow.find_element(*PlanPage.runFull).click()

    def RunIncremental(self,planRow):
        return planRow.find_element(*PlanPage.runIncremental).click()
        
    def ClosePlanDashboard(self):
        return self.driver.find_element(*PlanPage.closePlanDashboard).click()

    def HowToProtect(self):
        return self.driver.find_element(*PlanPage.howToProtect).click()
    
    def FileLevel(self):
        return self.driver.find_element(*PlanPage.fileLevel).click()

    def ImageLevel(self):
        return self.driver.find_element(*PlanPage.imageLevel).click()

    def WhichDevices(self):
        return self.driver.find_element(*PlanPage.whichDevices).click()

    def MainDeviceCheckbox(self,main):
        return main.find_element(*PlanPage.mainDeviceCheckbox).click()

    def ApplyButton(self):
        return self.driver.find_element(*PlanPage.applyButton).click()

    def WhatToProtect(self):
        return self.driver.find_element(*PlanPage.whatToProtect).click()

    def DeviceName(self):
        return self.driver.find_element(*PlanPage.deviceName).click()

    def DiskCheckBox(self,diskletter):
        return diskletter.find_element(*PlanPage.diskCheckbox).click()

    def SaveChoice(self):
        return self.driver.find_element(*PlanPage.saveChoice).click()

    def WhereToStore(self):
        return self.driver.find_element(*PlanPage.whereToStore).click()

    def XoperoStorage(self):
        return self.driver.find_element(*PlanPage.xoperoStorage).click()
        
    def When(self):
        return self.driver.find_element(*PlanPage.when).click()

    def StartAt(self):
        return self.driver.find_element(*PlanPage.startAt)

    def SaveRun(self):
        return self.driver.find_element(*PlanPage.saveRun).click()
    
    def Next(self):
        return self.driver.find_element(*PlanPage.next).click()

    def SaveSchedule(self):
        return self.driver.find_element(*PlanPage.saveSchedule).click()






    
