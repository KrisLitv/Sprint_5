import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from data import TestUrls

@pytest.fixture(scope='function')
def browser():
    options = ChromeOptions()

    driver = webdriver.Chrome(options=options)
    driver.get(TestUrls.main_url)
    yield driver
    driver.quit()

