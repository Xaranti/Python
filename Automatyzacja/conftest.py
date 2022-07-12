#regionImport
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#endregion

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="help text here"
    )

@pytest.fixture(scope="class")
def setupBrowser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")

    elif browser_name == "firefox":
        pass
        #firefox invocation

    else:
        pass
        #IE invo

    driver.get("https://3be5838c-0e80-4f15-9003-3a1d5b749330.testing.xopero.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()