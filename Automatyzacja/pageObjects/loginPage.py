from selenium.webdriver.common.by import By
import time

class LogInPage:

    login = (By.NAME, "login")
    password = (By.ID,'mat-input-1')
    submitButton = (By.XPATH,"//button[@type='submit']")

    def __init__(self,driver):
        self.driver = driver

    def logIn(self):
        time.sleep(1)
        self.driver.find_element(*LogInPage.login).send_keys('login')
        self.driver.find_element(*LogInPage.password).send_keys("password")
        self.driver.find_element(*LogInPage.submitButton).click()
        return
