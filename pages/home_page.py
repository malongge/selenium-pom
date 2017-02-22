from .base_page import BasePage
from .page import Page
from .index_page import FocusPicMixin
from selenium.webdriver.common.by import By
import re


class HomePage(FocusPicMixin, BasePage):
    _ad_intercept_close_loc = (By.CSS_SELECTOR, '#usercp_dltc_div a')
    _login_layer_frame_loc = (By.ID, 'login_layer')
    _index_link_loc = (By.CSS_SELECTOR, "#jycm_head_nav_links_sub li a[href='http://www.jiayuan.com/']")
    _left_float_loc = (By.CSS_SELECTOR, "#jy_cpfl_2_box .finance_redBox_img")
    _right_float_img_loc = (By.CSS_SELECTOR, "#jy_cpfl_1_box a img")
    _right_float_a_loc = (By.CSS_SELECTOR, "#jy_cpfl_1_box a")

    css_url_pat = re.compile(r'url\((.+)\)')

    @property
    def header(self):
        return self.Header(self.base_url, self.selenium)

    class Header(Page):
        _logout_locator = (By.CSS_SELECTOR, '#head_user_logout a')
        _user_name_locator = (By.CSS_SELECTOR, '#head_user_nickname a')

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._logout_locator)

        @property
        def username_text(self):
            return self.find_element(*self._user_name_locator).text

        def click_logout(self):
            self.find_element(*self._logout_locator).click()

    def close_ad_intercept(self):
        with self.focus_frame(self._login_layer_frame_loc):
            close_btn = self.find_element(*self._ad_intercept_close_loc)
            close_btn.click()

    def click_index_link(self):
        link = self.find_element(*self._index_link_loc)
        link.click()

    def get_left_float_links(self):
        a = self.find_element(*self._left_float_loc)
        href = a.get_attribute('href')
        css_prop = a.value_of_css_property('background')
        groups = self.css_url_pat.findall(css_prop)
        url = groups[0] if groups else None
        print(href, url)
        return href, url.replace('"', "")

    def get_right_float_links(self):
        a = self.find_element(*self._right_float_a_loc)
        href = a.get_attribute('href')
        img = self.find_element(*self._right_float_img_loc)
        link = img.get_attribute('src')
        print(href, link)
        return href, link
