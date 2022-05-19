from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time


def kontrolaZadania(driver):
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

def podsumowanie(driver):
    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'Tasks')]").click() #wybór zadań
        driver.find_element(By.XPATH,"//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań

        ##########################################
        statuses = ["OK","warnings","errors"]
        for status in statuses:
            attribute = driver.find_element(By.XPATH,"//span[text()='%s']" %(status))
            result = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(attribute)).text
            print(status,":",result)

        # OK = driver.find_element(By.XPATH,"//span[text()='OK']")
        # Success = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(OK)).text

        # warning = driver.find_element(By.XPATH,"//span[text()='warnings']")
        # warnResult = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(warning)).text

        # NOK = driver.find_element(By.XPATH,"//span[text()='errors']")
        # errors = driver.find_element(locate_with(By.CLASS_NAME,  "count").above(NOK)).text

        # print("         Podsumowanie wykonania zadania: Pass")
        # print("         Pomyślnie zakończono %s zadań" %(Success))
        # print("         Ostrzeżeniami zakończono %s zadań " %(warnResult))
        # print("         Błędami zakończono %s zadań" %(errors))

    except:
        print("Podsumowanie wykonania zadania: Failed")
    return()