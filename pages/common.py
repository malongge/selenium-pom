from selenium.webdriver.common.by import By

from pages.unlogin_page import UnloginPage


def _login(base_url, selenium, PageClass, user_dict):

    unlogin_pg = UnloginPage(base_url, selenium)
    home_pg = PageClass(base_url, selenium)
    unlogin_pg.get_relative_path('/')
    unlogin_pg.maximize_window()
    unlogin_pg.header.login(user_dict['username'], user_dict['password'])
    home_pg.wait_for_element_to_be_visible(By.ID, 'jycm_head_nav')
    return unlogin_pg, home_pg
