from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthLocators
from data import TestUrls

from faker import Faker

fake = Faker()

class TestDataHelpers:
    @staticmethod
    def email():
        name = fake.first_name()
        surname = fake.last_name()
        domain = "ya.ru"
        email = f"{name.lower()}_{surname.lower()}@{domain}"
        return email, name

    @staticmethod
    def generate_correct_password_six_symbols(min_length=6):
        password = fake.password(length=max(min_length, 6))
        return password

    @staticmethod
    def generate_correct_password_more_then_six_symbols(min_length=6):
        password_length = fake.random_int(min=min_length, max=min_length + 10)
        password = fake.password(length=password_length)
        return password

    @staticmethod
    def generate_uncorrect_password_less_then_six_symbols(max_length=5):
        password_length = fake.random_int(min=4, max=max_length)
        password = fake.password(length=password_length)
        return password

    valid_email_for_login = 'kristinazhukova_7_277@yandex.ru'
    valid_password_for_login = 'Kafka5121'

def login(browser):
    browser.find_element(*AuthLocators.EMAIL_INPUT_LOGIN).send_keys(TestDataHelpers.valid_email_for_login)
    browser.find_element(*AuthLocators.PASSWORD_INPUT_LOGIN).send_keys(TestDataHelpers.valid_password_for_login)
    browser.find_element(*AuthLocators.LOGIN_BUTTON_LOGIN).click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(AuthLocators.MAKE_ORDER_BUTTON))

def registration(browser, name, email, password):
    browser.get(TestUrls.register_url)
    browser.find_element(*AuthLocators.NAME_INPUT_REGISTRATION).send_keys(name)
    browser.find_element(*AuthLocators.EMAIL_INPUT_REGISTRATION).send_keys(email)
    browser.find_element(*AuthLocators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
    browser.find_element(*AuthLocators.REGISTRATION_BUTTON).click()