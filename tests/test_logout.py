from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:

    def test_logout(self, driver, wait):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        driver.find_element(*Locators.EMAIL).send_keys("user@mail.com")
        driver.find_element(*Locators.PASSWORD).send_keys("Password123")
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        login_btn = wait.until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert login_btn is not None