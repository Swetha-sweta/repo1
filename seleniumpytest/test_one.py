import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

driver= None

@pytest.fixture(autouse=True)
def set_up_and_teardown():
    global driver
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield
    driver.quit()


def test_login_with_valid_credentials():

    driver.find_element("xpath", "//a[.='Log in']").click()
    driver.find_element("id", "Email").send_keys("swethasunithran@gmail.com")
    driver.find_element("id", "Password").send_keys("Swestha@123")
    driver.find_element("xpath", "//input[@value='Log in']").click()
    assert driver.find_element("xpath", "//a[.='swethasunithran@gmail.com']").is_displayed()

def test_login_with_invalid_credentials():

    driver.find_element("xpath", "//a[.='Log in']").click()
    driver.find_element("id", "Email").send_keys("swethasunithran@gmail.com")
    driver.find_element("id", "Password").send_keys("Swestha@123")
    driver.find_element("xpath", "//input[@value='Log in']").click()
    assert driver.find_element("xpath", "//a[.='swethasunithran@gmail.com']").is_displayed()



