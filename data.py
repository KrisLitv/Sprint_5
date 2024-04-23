from faker import Faker
fake = Faker()


class TestData:
    def email():
        name = fake.first_name()
        surname = fake.last_name()
        domain = "ya.ru"
        email = f"{name.lower()}_{surname.lower()}@{domain}"
        return email, name

    def generate_correct_password_six_symbols(min_length=6):
        fake = Faker()
        password = fake.password(length=max(min_length, 6))
        return password
    def generate_correct_password_more_then_six_symbols(min_length=6):
        fake = Faker()
        password_length = fake.random_int(min=min_length,max=min_length + 10)
        password = fake.password(length=password_length)
        return password
    def generate_uncorrect_password_less_then_six_symbols(max_length=5):
        fake = Faker()
        password_length = fake.random_int(min=4, max=max_length)
        password = fake.password(length=password_length)
        return password

    valid_email_for_login = 'kristinazhukova_7_277@yandex.ru'
    valid_password_for_login = 'Kafka5121'


class TestUrls:

    base_url = 'https://stellarburgers.nomoreparties.site/'

    main_url = base_url
    register_url = base_url + 'register'
    login_url = base_url + 'login'
    forgot_password_url = base_url + 'forgot-password'


class TestConstructorNavigationText:
    buns_navigation_text = 'Булки'
    sauces_navigation_text = 'Соусы'
    filler_navigation_text = 'Начинки'

