from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestAds:

    def login(self, driver, wait, email="user@mail.com", password="Password123"):
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

    def test_create_ad_unauthorized(self, driver, wait):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BUTTON)).click()
        popup = wait.until(EC.visibility_of_element_located(Locators.POPUP))
        assert popup.is_displayed()
        
    
    def test_create_ad_authorized(self, driver, wait, authorized_user):
        wait.until(EC.visibility_of_element_located(Locators.USER_NAME))

        create_btn = wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BUTTON))
        driver.execute_script("arguments[0].click();", create_btn)

        title = "12345"

        wait.until(EC.visibility_of_element_located(Locators.AD_TITLE_INPUT)).send_keys(title)

        description = wait.until(EC.visibility_of_element_located(Locators.AD_DESCRIPTION))
        driver.execute_script("arguments[0].scrollIntoView();", description)
        description.send_keys("test")

        wait.until(EC.visibility_of_element_located(Locators.AD_PRICE)).send_keys("12345")

        wait.until(EC.element_to_be_clickable(Locators.CATEGORY_DROPDOWN)).click()
        wait.until(EC.visibility_of_element_located(Locators.CATEGORY_BOOKS)).click()

        wait.until(EC.element_to_be_clickable(Locators.CITY_DROPDOWN)).click()
        wait.until(EC.visibility_of_element_located(Locators.CITY_OPTION)).click()

        wait.until(EC.element_to_be_clickable(Locators.CONDITION_USED)).click()

        publish_btn = wait.until(EC.presence_of_element_located(Locators.PUBLISH))
        driver.execute_script("arguments[0].scrollIntoView();", publish_btn)
        driver.execute_script("arguments[0].click();", publish_btn)

        wait.until(EC.staleness_of(publish_btn))

        wait.until(EC.visibility_of_element_located(Locators.CREATE_AD_BUTTON))

        profile_btn = wait.until(EC.presence_of_element_located(Locators.PROFILE))
        driver.execute_script("arguments[0].click();", profile_btn)

        ads = wait.until(EC.visibility_of_all_elements_located(Locators.AD_CARD))
        
        assert any(title in ad.text for ad in ads)
