from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)

###############TEST 1 - Logowanie ####################
def logowanie():
    try:
        driver.get("http://localhost:28555") # <-- url usługi
        driver.maximize_window()
        time.sleep(2)

    
        log = driver.find_element(By.NAME,'login')
        log.send_keys('admin@xopero.com') # <-- login
        time.sleep(1)

        pas = driver.find_element(By.ID,'mat-input-1')
        pas.send_keys("Admin_123") #<-- hasło

        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(1)
        title = driver.current_url

        if title == 'http://localhost:28555/devices':
            print ("Test 1 - Logowanie: Pass")
            return

        else:
            print("Test 1 - Logowanie: Failed")
            return

    except:
        print("Test 1 - Logowanie: Failed")
        exit()


def kontrolaZadania():
    try:
        time.sleep(1)
        print("     Zadanie w trakcie wykonywania")
        x = True

        while x:
            if driver.find_element(By.XPATH,'//*[@id="mat-badge-content-7"]').is_displayed():
                time.sleep(5)
            else:
                x = False

        try:
            driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[2]/aside/app-aside/ng-component/app-dashboard-plan/div/div[1]/app-close-aside-button/button').click()
        except:
            pass

        print("     Zakończono zadanie")
        return
    except:
        return


def podsumowanie():
    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań
        driver.find_element(By.XPATH,"//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań

        ##########################################
        OK = driver.find_element(By.XPATH,"//span[text()='OK']")
        Success = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(OK)).text

        warning = driver.find_element(By.XPATH,"//span[text()='warnings']")
        warnResult = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(warning)).text

        NOK = driver.find_element(By.XPATH,"//span[text()='errors']")
        errors = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(NOK)).text

        print("         Podsumowanie wykonania zadania: Pass")
        print("         Pomyślnie zakończono %s zadań" %(Success))
        print("         Ostrzeżeniami zakończono %s zadań " %(warnResult))
        print("         Błędami zakończono %s zadań" %(errors))

    except:
        print("Podsumowanie wykonania zadania: Failed")
    return

def fileBackupCLD():
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"//*[contains(text(),'Plans')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'Add plan')]").click()

    driver.find_element(By.NAME,"backupPlanName").clear()
    driver.find_element(By.NAME,"backupPlanName").send_keys("File backup on Cloud")

    driver.find_element(By.XPATH,"//*[contains(text(),'How to protect')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'File-level')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'Which devices?')]").click()

    mainDevice = driver.find_element(By.XPATH,"//span[text()='Main']/../../..")
    mainDevice.find_element(By.CLASS_NAME, "mat-checkbox").click()

    driver.find_element(By.XPATH,"//*[contains(text(),'Apply')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'What to protect?')]").click()

    driver.find_element(By.XPATH,'/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-add-rule/div/div[3]/div[2]/div[2]/div/h3').click()
         

    folderTree = driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[3]/app-aside/ng-component/app-add-device-rule/div/div[2]/app-files-browser/app-files/ul")
    y = R"D:\pliki\jsony jira" ##<--- wstaw ścieżkę backupu
    y=y.replace(":","")
    backupPath = y.split("\\")
    fileName = backupPath.pop(-1)

    for folder in backupPath:
        folderName = folderTree.find_element(By.XPATH,"//span[text()='%s']/../.." %(folder)) 
        folderName.find_element(By.CSS_SELECTOR,"svg[data-icon='plus']").click()

    fileNameElem = folderTree.find_element(By.XPATH,"//*[contains(text(),'%s')]" %(fileName))
    driver.find_element(locate_with(By.CLASS_NAME,  "mat-checkbox-layout").to_left_of(fileNameElem)).click()
    
    driver.find_element(By.XPATH,"/html/body/app-root/app-main/div/app-content/div[1]/aside[3]/app-aside/ng-component/app-add-device-rule/div/div[3]/button/span[1]").click()
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

    # kontrolaZadania()
    # podsumowanie()

    return()

logowanie()
fileBackupCLD()

