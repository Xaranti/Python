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
        self.driver.find_element(*LogInPage.login).send_keys('m.stasiak+130@xopero.com')
        self.driver.find_element(*LogInPage.password).send_keys("OM&Di<qNhW~81{(JFQc_SL2[Yp0g>Trw")
        self.driver.find_element(*LogInPage.submitButton).click()
        return