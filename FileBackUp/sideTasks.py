from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

def logowanie(driver):
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


