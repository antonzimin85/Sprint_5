from selenium.webdriver.common.by import By

class LoginPageLocators:

    ENTER_AND_REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Вход и регистрация"]')

    NO_ACCOUNT_BUTTON_ON_ENTER_POPUP = (By.XPATH, './/button[text()="Нет аккаунта"]')
    ENTER_EMAIL_FIELD_ON_ENTER_POPUP = (By.XPATH, './/input[@name="email"]')
    ENTER_EMAIL_FIELD_BORDER_ON_ENTER_POPUP = (By.XPATH, './/input[@name="email"]/parent::div')

    ENTER_PASSWORD_FIELD_ON_ENTER_POPUP = (By.XPATH, './/input[@name="password"]')
    ENTER_PASSWORD_FIELD_BORDER_ON_ENTER_POPUP = (By.XPATH, './/input[@name="password"]/parent::div')
    ENTER_REPEAT_PASSWORD_FIELD_ON_ENTER_POPUP = (By.XPATH, './/input[@name="submitPassword"]')
    ENTER_REPEAT_PASSWORD_FIELD_BORDER_ON_ENTER_POPUP = (By.XPATH, './/input[@name="submitPassword"]/parent::div')

    CREATE_ACCOUNT_BUTTON_ON_ENTER_POPUP = (By.XPATH, './/button[text()="Создать аккаунт"]')
    ENTER_BUTTON_ON_ENTER_POPUP = (By.XPATH, './/button[text()="Войти"]')
    VALIDATION_ERROR = (By.XPATH, './/span[text()="Ошибка"]')
    AUTHORIZE_TITLE_ON_ENTER_POPUP = (By.XPATH, './/h1[text()="Чтобы разместить объявление, авторизуйтесь"]')

    PRODUCT_NAME_INPUT_FIELD = (By.XPATH, './/input[@name="name"]')
    PRODUCT_DESCRIPTION_INPUT_FIELD = (By.XPATH, './/textarea[@name="description"]')
    PRODUCT_PRICE_INPUT_FIELD = (By.XPATH, './/input[@name="price"]')
    PRODUCT_CATEGORY_DROPDOWN = (By.XPATH, './/input[@name="category"]/following-sibling::button')
    PRODUCT_CATEGORY_DROPDOWN_HOBBY_ITEM = (By.XPATH, './/span[text()="Хобби"]')
    CITY_DROPDOWN = (By.XPATH, './/input[@name="city"]/following-sibling::button')
    CITY_DROPDOWN_KAZAN = (By.XPATH, './/span[text()="Казань"]/parent::button')
    USED_PRODUCT_CONDITION_RADIOBUTTON = (By.XPATH, './/input[@name="condition" and @value="Б/У"]/following-sibling::div')
    PUBLISH_AD_BUTTON = (By.XPATH, './/button[text()="Опубликовать"]')
    MY_PROFILE_TITLE = (By.XPATH, './/h1[text()="Мой профиль"]')

    USER_AD_PRODUCT_NAME = (By.XPATH, './/div[@class="card"][1]//div[@class="about"]/h2')
    USER_AD_CITY = (By.XPATH, './/div[@class="card"][1]//div[@class="about"]/h3')
    USER_AD_PRODUCT_PRICE = (By.XPATH, './/div[@class="card"][1]//div[@class="price"]/h2')

    SUBMIT_BUTTON = (By.XPATH, './/button[text()="Применить"]')
    MY_ADS_TITLE = (By.XPATH, './/h1[text()="Мои объявления"]')

    CREATE_AD_BUTTON_IN_HEADER = (By.XPATH, './/button[text()="Разместить объявление"]')
    USER_AVATAR_IN_HEADER = (By.XPATH, './/button[@class="circleSmall"]')
    USER_NAME_IN_HEADER = (By.XPATH, './/h3[@class="profileText name"]')
    LOGOUT_BUTTON_IN_HEADER = (By.XPATH, './/button[text()="Выйти"]')
