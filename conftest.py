import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium


@pytest.fixture
def stored_users(variables):
    return variables['users']


@pytest.fixture
def existing_user(stored_users):
    return stored_users['default']


@pytest.fixture
def nophone_user(stored_users):
    return stored_users['nophone']


@pytest.fixture
def uid_cookie(stored_users):
    return stored_users['cookie']


def _login(base_url, selenium, PageClass, user_dict):
    from pages.unlogin_page import UnloginPage
    from selenium.webdriver.common.by import By
    unlogin_pg = UnloginPage(base_url, selenium)
    home_pg = PageClass(base_url, selenium)
    unlogin_pg.get_relative_path('/')
    unlogin_pg.maximize_window()
    unlogin_pg.header.login(user_dict['username'], user_dict['password'])
    home_pg.wait_for_element_to_be_visible(By.ID, 'jycm_head_nav')
    return unlogin_pg, home_pg


@pytest.fixture(scope='function')
def login(base_url, selenium, existing_user):
    from pages.home_page import HomePage
    return _login(base_url, selenium, HomePage, existing_user)


@pytest.fixture(scope='function')
def nophone_login(base_url, selenium, nophone_user):
    from pages.home_page import NoPhoneHomePage
    return _login(base_url, selenium, NoPhoneHomePage, nophone_user)


def pytest_addoption(parser):
    parser.addini('custom_value', 'documentation of my custom value')
