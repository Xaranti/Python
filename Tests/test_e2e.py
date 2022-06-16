#regionImport
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage
#endregion

class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItem()
        cards = checkoutpage.getCardTitles()
        i=-1
        for card in cards:
            i=i+1
            cardText = card.text
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.Checkout().click()

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID,"country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text

        assert  ("Success" in textMatch)

