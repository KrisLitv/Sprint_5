
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthLocators
from helpers import TestDataHelpers
from helpers import registration
from conftest import browser


class TestRegistration:

    def test_registration_success_by_password_six_symbols(self, browser):



        email, name = TestDataHelpers.email()
        password = TestDataHelpers.generate_correct_password_six_symbols()
        registration(browser, name, email,password)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AuthLocators.LOGIN_BUTTON_LOGIN))
        assert browser.find_element(*AuthLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

    def test_registration_success_by_password_more_then_six_symbols(self, browser):



        email, name = TestDataHelpers.email()
        password = TestDataHelpers.generate_correct_password_more_then_six_symbols()
        registration(browser, name, email, password)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AuthLocators.LOGIN_BUTTON_LOGIN))
        assert browser.find_element(*AuthLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

    def test_registration_failed_error(self, browser):



        email, name = TestDataHelpers.email()
        password = TestDataHelpers.generate_uncorrect_password_less_then_six_symbols()
        registration(browser, name, email, password)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AuthLocators.PASSWORD_INPUT_ERROR_REGISTRATION))
        expected_text = "Некорректный пароль"
        assert browser.find_element(*AuthLocators.PASSWORD_INPUT_ERROR_REGISTRATION).text == expected_text
