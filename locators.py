from selenium.webdriver.common.by import By

class MainPageLocators:


    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"
    LOGO_MAIN = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"

    BUNS_BUTTON = By.XPATH, ".//span[text()='Булки']"
    SAUCES_BUTTON = By.XPATH, ".//span[text()='Соусы']"
    FILLER_BUTTON = By.XPATH, ".//span[text()='Начинки']"

    BUNS_BANNER = By.XPATH, ".//h2[text()='Булки']"
    SAUCES_BANNER = By.XPATH, ".//h2[text()='Соусы']"
    TOPPINGS_BANNER = By.XPATH, ".//h2[text()='Начинки']"

    CURRENT_TAB = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]"
    MAKE_BURGER_BANNER = By.XPATH, ".//h1[text()='Соберите бургер']"



class AuthLocators:

    NAME_INPUT_REGISTRATION = By.XPATH, "//label[text() = 'Имя']/following-sibling::input"
    EMAIL_INPUT_REGISTRATION = By.XPATH, "//label[text() = 'Email']/following-sibling::input"
    PASSWORD_INPUT_REGISTRATION = By.XPATH, "//label[text() = 'Пароль']/following-sibling::input"
    REGISTRATION_BUTTON = By.XPATH, "//button[text() = 'Зарегистрироваться']"
    LOGIN_BUTTON_REGISTRATION = By.XPATH, ".//a[text()='Войти']"
    PASSWORD_INPUT_ERROR_REGISTRATION = By.XPATH, ".//p[text()='Некорректный пароль']"
    LINK_TO_REGISTRATION_PAGE_FROM_ACCOUNT = By.XPATH, ".//a[@class = 'Auth_link__1fOlj']"

    LOGIN_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    EMAIL_INPUT_LOGIN = By.XPATH, "//input[@name = 'name']"
    PASSWORD_INPUT_LOGIN = By.XPATH, "//input[@name = 'Пароль']"
    LOGIN_BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"
    LOGIN_BANNER = By.XPATH, ".//h2[text()='Вход']"
    LOGIN_BUTTON_RECOVERY = By.XPATH, ".//a[text()='Войти']"
    HEADING_ON_LOG_IN_PAGE = By.XPATH, ".//h2[text() ='Вход']"

    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ACCOUNT_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"

