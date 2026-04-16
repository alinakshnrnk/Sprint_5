from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from email_generator import generate_email


class TestRegistration:

    def test_success_registration(self, driver, wait):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        email = generate_email()

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        email_field = wait.until(EC.visibility_of_element_located(Locators.EMAIL))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.visibility_of_element_located(Locators.PASSWORD))
        password_field.send_keys("Password123")

        repeat_field = wait.until(EC.visibility_of_element_located(Locators.REPEAT_PASSWORD))
        repeat_field.send_keys("Password123")

        wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT)).click()

        wait.until(EC.invisibility_of_element_located(Locators.CREATE_ACCOUNT))

        user = wait.until(EC.visibility_of_element_located(Locators.USER_NAME)).text
        assert user == "User."

    def test_invalid_email(self, driver, wait):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(Locators.EMAIL)).send_keys("invalid")
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD)).send_keys("123")
        wait.until(EC.element_to_be_clickable(Locators.REPEAT_PASSWORD)).send_keys("123")

        wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT)).click()

        error = wait.until(EC.visibility_of_element_located(Locators.ERROR))
        assert error.is_displayed()

    def test_existing_user(self, driver, wait):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys("user@mail.com")
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD)).send_keys("Password123")
        wait.until(EC.visibility_of_element_located(Locators.REPEAT_PASSWORD)).send_keys("Password123")

        wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT)).click()

        error = wait.until(EC.visibility_of_element_located(Locators.ERROR))
        assert error.is_displayed()