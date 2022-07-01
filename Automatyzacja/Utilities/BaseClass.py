import pytest
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setupBrowser")

class BaseClass:

    def verifyLinkPresence(self,text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.link,text)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger