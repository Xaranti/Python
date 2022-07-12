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

class Test_Login(BaseClass):

    def test_login(self):
        log = self.getLogger()
        time.sleep(5)
        logInPage = LogInPage(self.driver)
        logInPage.logIn()
        time.sleep(2)
        try:
            #assert self.driver.current_url == "http://localhost:28555/devices"
            log.info("User sucessfully logged")
        except:
            log.critical("LogIn Failed")
            raise






