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


from pages.common import _login

@pytest.fixture(scope='function')
def login(base_url, selenium, existing_user):
    from pages.home_page import HomePage
    return _login(base_url, selenium, HomePage, existing_user)

@pytest.fixture(scope='function')
def nophone_login(base_url, selenium, nophone_user):
    from pages.home_page import NoPhoneHomePage
    return _login(base_url, selenium, NoPhoneHomePage, nophone_user)

@pytest.fixture(scope='function')
def unlogin_page(base_url, selenium, uid_cookie):
    from pages.unlogin_page import UnloginPage
    ulg = UnloginPage(base_url, selenium)
    # 注入 my_uid cookie, 有 cookie 和没有 cookie 的情况页面展示不一样
    ulg.get_cookie_index_page('/', uid_cookie)
    return ulg



def pytest_addoption(parser):
    parser.addini('custom_value', 'documentation of my custom value')

#
# def pytest_runtest_setup(item):
#     print(item.__dict__)
#     if 'once' in item.name and not item.config.getoption("--once"):
#         pytest.skip("need --once option to run")

