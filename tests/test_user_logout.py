from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LoginPageLocators
from config import BASE_URL, MAIN_URL

class TestUserLogout:

    def test_user_logout_existing_user_user_is_logged_out(self, webdriver_instance, existing_user_credentials):

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
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON_IN_HEADER))
        webdriver_instance.find_element(*LoginPageLocators.LOGOUT_BUTTON_IN_HEADER).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON))
        enter_and_registration_button = webdriver_instance.find_element(*LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON)

        assert enter_and_registration_button.is_displayed()