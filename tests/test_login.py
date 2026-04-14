from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_login(self, driver, wait):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys("user@mail.com")
        driver.find_element(*Locators.PASSWORD).send_keys("Password123")

        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        user = wait.until(EC.visibility_of_element_located(Locators.USER_NAME)).text

        assert user == "User."