import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def authorized_user(driver, wait):

    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    
    wait.until(EC.element_to_be_clickable(Locators.EMAIL)).send_keys("user@mail.com")
    wait.until(EC.element_to_be_clickable(Locators.PASSWORD)).send_keys("Password123")
    
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_SUBMIT)).click()
    
    wait.until(EC.visibility_of_element_located(Locators.AVATAR))