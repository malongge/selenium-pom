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
def uid_cookie(stored_users):
    return stored_users['cookie']


@pytest.fixture(scope='function')
def login(base_url, selenium, existing_user):
    from pages.index_page import IndexPage
    login_pg = IndexPage(base_url, selenium)
    login_pg.header.login(existing_user['username'], existing_user['password'])
