from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LoginPageLocators
from config import BASE_URL, PROFILE_URL

class TestAdCreation:

    def test_ad_creation_unregistered_user_modal_window_with_title_is_displayed(self, webdriver_instance):
        webdriver_instance.get(BASE_URL)
        webdriver_instance.find_element(*LoginPageLocators.CREATE_AD_BUTTON_IN_HEADER).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.AUTHORIZE_TITLE_ON_ENTER_POPUP))
        authorize_title_text = webdriver_instance.find_element(*LoginPageLocators.AUTHORIZE_TITLE_ON_ENTER_POPUP).text
        expected_authorize_title_text = 'Чтобы разместить объявление, авторизуйтесь'

        assert authorize_title_text == expected_authorize_title_text

        webdriver_instance.quit()

    def test_ad_creation_registered_user_ad_is_created(self, webdriver_instance, existing_user_credentials, product_with_attributes):
        webdriver_instance.get(BASE_URL)
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON))
        webdriver_instance.find_element(*LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_EMAIL_FIELD_ON_ENTER_POPUP))
        existing_user_email, existing_user_password = existing_user_credentials

        webdriver_instance.find_element(*LoginPageLocators.ENTER_EMAIL_FIELD_ON_ENTER_POPUP).send_keys(existing_user_email)
        webdriver_instance.find_element(*LoginPageLocators.ENTER_PASSWORD_FIELD_ON_ENTER_POPUP).send_keys(
            existing_user_password)
        webdriver_instance.find_element(*LoginPageLocators.ENTER_BUTTON_ON_ENTER_POPUP).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.USER_NAME_IN_HEADER))
        webdriver_instance.find_element(*LoginPageLocators.CREATE_AD_BUTTON_IN_HEADER).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.PRODUCT_NAME_INPUT_FIELD))
        product_name, product_description, product_price = product_with_attributes
        webdriver_instance.find_element(*LoginPageLocators.PRODUCT_NAME_INPUT_FIELD).send_keys(product_name)
        webdriver_instance.find_element(*LoginPageLocators.PRODUCT_DESCRIPTION_INPUT_FIELD).send_keys(product_description)
        webdriver_instance.find_element(*LoginPageLocators.PRODUCT_PRICE_INPUT_FIELD).send_keys(product_price)
        webdriver_instance.find_element(*LoginPageLocators.PRODUCT_CATEGORY_DROPDOWN).click()
        webdriver_instance.find_element(*LoginPageLocators.PRODUCT_CATEGORY_DROPDOWN_HOBBY_ITEM).click()
        webdriver_instance.find_element(*LoginPageLocators.CITY_DROPDOWN).click()
        webdriver_instance.find_element(*LoginPageLocators.CITY_DROPDOWN_KAZAN).click()
        webdriver_instance.find_element(*LoginPageLocators.USED_PRODUCT_CONDITION_RADIOBUTTON).click()
        webdriver_instance.find_element(*LoginPageLocators.PUBLISH_AD_BUTTON).click()
        WebDriverWait(webdriver_instance, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
        webdriver_instance.find_element(*LoginPageLocators.USER_AVATAR_IN_HEADER).click()
        WebDriverWait(webdriver_instance, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.USER_AD_PRODUCT_NAME))
        user_ad_product_name = webdriver_instance.find_element(*LoginPageLocators.USER_AD_PRODUCT_NAME).text
        user_ad_city = webdriver_instance.find_element(*LoginPageLocators.USER_AD_CITY).text
        user_ad_product_price = webdriver_instance.find_element(*LoginPageLocators.USER_AD_PRODUCT_PRICE).text
        expected_user_ad_city = 'Казань'

        assert webdriver_instance.current_url == PROFILE_URL
        assert user_ad_product_name == product_name
        assert user_ad_product_price == f'{product_price} ₽'
        assert user_ad_city == expected_user_ad_city

        webdriver_instance.quit()
