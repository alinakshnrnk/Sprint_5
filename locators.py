from selenium.webdriver.common.by import By


class Locators:

    # главная / авторизация
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")
    CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

    # поля
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.NAME, "password")
    REPEAT_PASSWORD = (By.NAME, "submitPassword")

    # пользователь
    USER_NAME = (By.CSS_SELECTOR, ".profileText.name")
    AVATAR = (By.CLASS_NAME, "circleSmall")

    # ошибки
    ERROR = (By.XPATH, "//span[text()='Ошибка']")

    # создание объявления
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    AD_TITLE_INPUT = (By.NAME, "name")
    AD_DESCRIPTION = (By.XPATH, ".//textarea[@name='description']")
    AD_PRICE = (By.NAME, "price")

    CITY_DROPDOWN = (By.XPATH, "(//button[contains(@class,'dropDownMenu_arrowDown')])[2]")
    CITY_OPTION = (By.XPATH, "//div[contains(@class,'dropDownMenu_options')]//span[text()='Новосибирск']")

    CATEGORY_DROPDOWN = (By.XPATH, "(//button[contains(@class,'dropDownMenu_arrowDown')])[1]")
    CATEGORY_BOOKS = (By.XPATH, "//div[contains(@class,'dropDownMenu_options')]//span[text()='Книги']")

    CONDITION_USED = (By.XPATH, "//label[text()='Б/У']")
    PUBLISH = (By.XPATH, "//button[@type='submit' and text()='Опубликовать']")

    PROFILE = (By.CLASS_NAME, "circleSmall")
    AD_CARD = (By.XPATH, "//div[@class='card']//h2")

    # popup
    POPUP = (By.XPATH, "//h1[contains(text(),'Чтобы разместить объявление')]")