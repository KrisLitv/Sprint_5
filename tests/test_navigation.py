from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, AuthLocators
from data import TestUrls
from conftest import browser

class TestNavigation:

    def test_go_to_account_from_main_page(self, browser):



        browser.find_element(*AuthLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located(AuthLocators.LOGIN_BUTTON_LOGIN))
        assert browser.current_url == TestUrls.login_url

    def test_go_to_constructor_from_account_on_button(self, browser):



        browser.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.MAKE_BURGER_BANNER))
        assert browser.current_url == TestUrls.main_url

    def test_go_to_constructor_from_account_on_logo(self, browser):



        browser.find_element(*MainPageLocators.LOGO_MAIN).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.MAKE_BURGER_BANNER))
        assert browser.current_url == TestUrls.main_url
