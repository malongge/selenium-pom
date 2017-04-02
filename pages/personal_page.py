import time

from selenium.webdriver.common.by import By

from .login_page import _LoginPage


class PersonalPage(_LoginPage):

    _right_top_ad_a_loc = (By.CSS_SELECTOR, '#jy_ad_3034 a')
    _right_middle_recommend_service_ad_loc = (By.CSS_SELECTOR, '.my_service_buy a')
    _self_description_right_hand_ad_loc = (By.CSS_SELECTOR, '#ad_pos_pcweb_102 a')

    def find_all_recommend_service_link(self):
        elems = self.find_elements(*self._right_middle_recommend_service_ad_loc)
        elem_links = []
        for elem in elems:
            elem_links.append(elem.get_attribute('href'))
        return elem_links








