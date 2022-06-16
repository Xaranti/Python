from selenium.webdriver.common.by import By

class CheckOutPage:

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    checkout = (By.CSS_SELECTOR,"a[class*='btn-primary']")

    def __init__(self,driver):
        self.driver=driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def Checkout(self):
        return self.driver.find_element(*CheckOutPage.checkout)