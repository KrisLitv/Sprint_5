
from locators import AuthLocators
from data import TestUrls
from helpers import login
from conftest import browser

class TestLogin:

    def test_login_from_main_page(self, browser):



        browser.find_element(*AuthLocators.LOGIN_ACCOUNT_BUTTON).click()
        login(browser)
        assert browser.find_element(*AuthLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_account_page(self, browser):



        browser.find_element(*AuthLocators.ACCOUNT_BUTTON).click()
        login(browser)
        assert browser.find_element(*AuthLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_registration_page(self, browser):



        browser.find_element(*AuthLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*AuthLocators.LINK_TO_REGISTRATION_PAGE_FROM_ACCOUNT).click()
        browser.find_element(*AuthLocators.LOGIN_BUTTON_REGISTRATION).click()
        login(browser)
        assert browser.find_element(*AuthLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_recovery_page(self, browser):



        browser.get(TestUrls.forgot_password_url)
        browser.find_element(*AuthLocators.LOGIN_BUTTON_RECOVERY).click()
        login(browser)
        assert browser.find_element(*AuthLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"
