from selenium.webdriver.common.by import By


class StoragePage:
    
    storagesPage = (By.XPATH,'/html/body/app-root/app-main/app-menu/section/nav[1]/a[6]')
    addStorage = (By.XPATH,'/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/ng-component/button/span[1]')
    storageName = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field/div/div[1]/div[2]/input")
    localPath = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-local/mat-form-field/div/div[1]/div/input")
    save = (By.XPATH,"//*[contains(text(),'Save')]")
    storageType = (By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/ng-select/div')
    networkLocation = (By.XPATH,"//*[contains(text(),'Network location')]")
    SMBuserName = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-smb/app-controlled-input/mat-form-field/div/div[1]/div[1]/input")
    selectPassword = (By.XPATH,"//*[contains(text(),'Select or add')]")
    addPassword = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-passwords-list-container/app-passwords-list/div/div[3]/button")
    passwordName = (By.NAME,"passwordName")
    passwords = (By.CSS_SELECTOR,"input[type='password']")
    smbPath = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-smb/mat-form-field/div/div[1]/div/input")
    nfsShare = (By.XPATH,"//*[contains(text(),'Network File Storage')]")
    nfsPath = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-nfs/app-controlled-input/mat-form-field/div/div[1]/div[1]/input")
    s3 = (By.XPATH,"//*[contains(text(),'S3 storage')]")
    s3Login = (By.XPATH,"//span[text()='Access key ID']/../../../input")
    s3serviceUrl = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-amazon/app-controlled-input[2]/mat-form-field/div/div[1]/div[1]/input")
    s3BucketName = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-amazon/app-controlled-input[3]/mat-form-field/div/div[1]/div[1]/input")
    Backblaze = (By.XPATH,"//*[contains(text(),'Backblaze B2')]")
    BackblazeBucket = (By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/div[2]/form/app-backblaze/app-controlled-input[2]/mat-form-field/div/div[1]/div[1]/input")

    def __init__(self,driver):
        self.driver = driver

    def storagePage(self):
        return self.driver.find_element(*StoragePage.storagesPage).click()
    
    def AddStorage(self):
        return self.driver.find_element(*StoragePage.addStorage).click()

    def StorageName(self):
        return self.driver.find_element(*StoragePage.storageName)

    def LocalPath(self):
        return self.driver.find_element(*StoragePage.localPath)

    def Save(self):
        return self.driver.find_element(*StoragePage.save).click()

    def StorageTypeSelect(self):
        return  self.driver.find_element(*StoragePage.storageType).click()

    def Type_SMB(self):
        return self.driver.find_element(*StoragePage.networkLocation).click()

    def SMBusername(self):
        return self.driver.find_element(*StoragePage.SMBuserName)

    def SelectPassword(self):
        return self.driver.find_element(*StoragePage.selectPassword).click()

    def AddNewPassword(self):
        return self.driver.find_element(*StoragePage.addPassword).click()

    def PasswordName(self):
        return self.driver.find_element(*StoragePage.passwordName)

    def Passwords(self):
        return self.driver.find_elements(*StoragePage.passwords)

    def SMBpath(self):
        return self.driver.find_element(*StoragePage.smbPath)

    def Type_NFS(self):
        return self.driver.find_element(*StoragePage.nfsShare).click()
    
    def NFSpath(self):
        return self.driver.find_element(*StoragePage.nfsPath)

    def S3(self):
        return self.driver.find_element(*StoragePage.s3).click()

    def LoginS3(self):
        return self.driver.find_element(*StoragePage.s3Login)

    def S3Url(self):
        return self.driver.find_element(*StoragePage.s3serviceUrl)

    def S3Bucket(self):
        return self.driver.find_element(*StoragePage.s3BucketName)

    def BackBlaze(self):
        return self.driver.find_element(*StoragePage.Backblaze).click()

    def BackBlazeBucket(self):
        return self.driver.find_element(*StoragePage.BackblazeBucket)







    

    