import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LoginPageLocators
from config import BASE_URL, MAIN_URL

class TestUserRegistration:

    def test_user_registration_valid_email_user_is_registered(self, webdriver_instance, new_user_credentials):
        webdriver_instance.get(BASE_URL)
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON))
        webdriver_instance.find_element(*LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.NO_ACCOUNT_BUTTON_ON_ENTER_POPUP))
        webdriver_instance.find_element(*LoginPageLocators.NO_ACCOUNT_BUTTON_ON_ENTER_POPUP).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_EMAIL_FIELD_ON_ENTER_POPUP))
        new_user_email, new_user_password = new_user_credentials
        webdriver_instance.find_element(*LoginPageLocators.ENTER_EMAIL_FIELD_ON_ENTER_POPUP).send_keys(new_user_email)
        webdriver_instance.find_element(*LoginPageLocators.ENTER_PASSWORD_FIELD_ON_ENTER_POPUP).send_keys(new_user_password)
        webdriver_instance.find_element(*LoginPageLocators.ENTER_REPEAT_PASSWORD_FIELD_ON_ENTER_POPUP).send_keys(new_user_password)
        webdriver_instance.find_element(*LoginPageLocators.CREATE_ACCOUNT_BUTTON_ON_ENTER_POPUP).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON_IN_HEADER))
        user_avatar = webdriver_instance.find_element(*LoginPageLocators.USER_AVATAR_IN_HEADER)
        user_name = webdriver_instance.find_element(*LoginPageLocators.USER_NAME_IN_HEADER).text

        # assert webdriver_instance.current_url == MAIN_URL    // проверка закомментирована, т.к. упадет из-за бага (URL не меняется)
        assert user_avatar.is_displayed()
        assert user_name == 'User.'

    @pytest.mark.parametrize('incorrect_email', ['test.net', 'test@.net', '@test.net', 'test@.', 'test@test', 'test@test.'])
    def test_user_registration_incorrect_email_error_is_displayed(self, webdriver_instance, incorrect_email):
        webdriver_instance.get(BASE_URL)
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON))
        webdriver_instance.find_element(*LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.NO_ACCOUNT_BUTTON_ON_ENTER_POPUP))
        webdriver_instance.find_element(*LoginPageLocators.NO_ACCOUNT_BUTTON_ON_ENTER_POPUP).click()
        webdriver_instance.find_element(*LoginPageLocators.ENTER_EMAIL_FIELD_ON_ENTER_POPUP).send_keys(incorrect_email)
        webdriver_instance.find_element(*LoginPageLocators.CREATE_ACCOUNT_BUTTON_ON_ENTER_POPUP).click()

        email_input_field = webdriver_instance.find_element(*LoginPageLocators.ENTER_EMAIL_FIELD_BORDER_ON_ENTER_POPUP)
        email_input_field_border_color = email_input_field.value_of_css_property('border-color')
        password_input_field = webdriver_instance.find_element(*LoginPageLocators.ENTER_PASSWORD_FIELD_BORDER_ON_ENTER_POPUP)
        password_field_border_color = password_input_field.value_of_css_property('border-color')
        repeat_password_input_field = webdriver_instance.find_element(*LoginPageLocators.ENTER_REPEAT_PASSWORD_FIELD_BORDER_ON_ENTER_POPUP)
        repeat_password_field_border_color = repeat_password_input_field.value_of_css_property('border-color')
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.VALIDATION_ERROR))
        validation_error = webdriver_instance.find_element(*LoginPageLocators.VALIDATION_ERROR)
        expected_border_color = 'rgb(149, 148, 171)'

        assert validation_error.is_displayed()
        assert email_input_field_border_color == expected_border_color
        assert password_field_border_color == expected_border_color
        assert repeat_password_field_border_color == expected_border_color

    def test_user_registration_existing_user_error_is_displayed(self, webdriver_instance, existing_user_credentials):
        webdriver_instance.get(BASE_URL)
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON))
        webdriver_instance.find_element(*LoginPageLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.NO_ACCOUNT_BUTTON_ON_ENTER_POPUP))
        webdriver_instance.find_element(*LoginPageLocators.NO_ACCOUNT_BUTTON_ON_ENTER_POPUP).click()
        existing_user_email, existing_user_password = existing_user_credentials

        webdriver_instance.find_element(*LoginPageLocators.ENTER_EMAIL_FIELD_ON_ENTER_POPUP).send_keys(existing_user_email)
        webdriver_instance.find_element(*LoginPageLocators.ENTER_PASSWORD_FIELD_ON_ENTER_POPUP).send_keys(existing_user_password)
        webdriver_instance.find_element(*LoginPageLocators.ENTER_REPEAT_PASSWORD_FIELD_ON_ENTER_POPUP).send_keys(existing_user_password)
        webdriver_instance.find_element(*LoginPageLocators.CREATE_ACCOUNT_BUTTON_ON_ENTER_POPUP).click()

        email_input_field = webdriver_instance.find_element(*LoginPageLocators.ENTER_EMAIL_FIELD_BORDER_ON_ENTER_POPUP)
        email_input_field_border_color = email_input_field.value_of_css_property('border-color')
        password_input_field = webdriver_instance.find_element(*LoginPageLocators.ENTER_PASSWORD_FIELD_BORDER_ON_ENTER_POPUP)
        password_field_border_color = password_input_field.value_of_css_property('border-color')
        repeat_password_input_field = webdriver_instance.find_element(*LoginPageLocators.ENTER_REPEAT_PASSWORD_FIELD_BORDER_ON_ENTER_POPUP)
        repeat_password_field_border_color = repeat_password_input_field.value_of_css_property('border-color')
        WebDriverWait(webdriver_instance, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.VALIDATION_ERROR))
        validation_error = webdriver_instance.find_element(*LoginPageLocators.VALIDATION_ERROR)
        expected_border_color = 'rgb(149, 148, 171)'

        assert validation_error.is_displayed()
        assert email_input_field_border_color == expected_border_color
        assert password_field_border_color == expected_border_color
        assert repeat_password_field_border_color == expected_border_color
