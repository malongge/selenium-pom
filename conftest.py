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


@pytest.fixture(scope='function')
def login(base_url, selenium, existing_user):
    from pages.index_page import IndexPage
    from pages.home_page import HomePage
    login_pg = IndexPage(base_url, selenium)
    home_pg = HomePage(base_url, selenium)
    login_pg.get_relative_path('/')
    login_pg.maximize_window()
    login_pg.header.login(existing_user['username'], existing_user['password'])
    home_pg.close_ad_intercept()
    return login_pg, home_pg


def pytest_addoption(parser):
    parser.addini('custom_value', 'documentation of my custom value')
