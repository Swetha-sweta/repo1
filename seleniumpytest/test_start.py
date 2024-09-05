import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture(autouse=True)
def launch_and_close():
    driver=WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    print("browser launched")
    yield
    driver.quit()
    print("browser closed")

@pytest.mark.priority1
def test_login_scenario():
    print("Executing login scenario...")

@pytest.mark.priority2
def test_register_scenario():
    print("Executing register scenario...")

@pytest.mark.priority1
def test_buy_14_inch_laptop():
    print("Executing buy 14 inch laptop")