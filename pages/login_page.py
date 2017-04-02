from .base_page import BasePage
from .page import Page
from selenium.webdriver.common.by import By
import re
import time


class _LoginPage(BasePage):

    # 弹框元素
    _ad_intercept_close_loc = (By.CSS_SELECTOR, '#usercp_dltc_div a')
    _login_layer_frame_loc = (By.ID, 'login_layer')

    # 导航栏元素
    _nav_link = "#jycm_head_nav_links_sub li a[href='{}']"

    # 左右浮层元素
    _left_float_loc = (By.ID, "jyfc_yx_left_a")
    _right_float_img_loc = (By.CSS_SELECTOR, "#jy_cpfl_1_box a img")
    _right_float_a_loc = (By.CSS_SELECTOR, "#jy_cpfl_1_box a")

    css_url_pat = re.compile(r'url\((.+)\)')

    # ad 元素
    _bottom_ad_a_log = (By.CSS_SELECTOR, "#ad_pos_pcweb_56 a")

    def nav_to_home_page(self):
        self.nav_to_page('http://usercp.jiayuan.com/')
        time.sleep(2)
        self.switch_to_second_window()

    def nav_to_index_page(self):
        self.nav_to_page('http://www.jiayuan.com/')
        time.sleep(2)
        self.switch_to_second_window()

    @property
    def header(self):
        return self.Header(self.base_url, self.selenium)

    class Header(Page):
        _logout_locator = (By.CSS_SELECTOR, '#head_user_logout a')
        _user_name_locator = (By.CSS_SELECTOR, '#head_user_nickname a')
        _uid_loc = (By.ID, 'head_user_uid')

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._logout_locator)

        @property
        def username_text(self):
            return self.find_element(*self._user_name_locator).text

        def click_logout(self):
            self.find_element(*self._logout_locator).click()

        def click_uid(self):
            self.find_element(*self._uid_loc).click()

    def nav_to_page(self, href):
        link = self.find_element(By.CSS_SELECTOR, self._nav_link.format(href))
        link.click()

    def is_login_layer_exist(self):
        return self.is_element_present(*self._login_layer_frame_loc)

    def close_ad_intercept(self):
        if self.is_login_layer_exist():
            try:
                with self.focus_frame(self._login_layer_frame_loc):
                    close_btn = self.find_element(*self._ad_intercept_close_loc)
                    close_btn.click()
                    return
            except Exception as e:  # 如果没有弹出拦截层直接不处理就行提高健壮性
                print("havephone", str(e))
            try:
                with self.focus_frame(self._login_layer_frame_loc):
                    nophone_close_btn = self.find_element(*self._ad_intercept_close_loc)
                    nophone_close_btn.click()
                    return
            except Exception as e:
                print("nophone", str(e))

    def get_left_float_links(self):
        self.wait_for_element_to_be_visible(*self._left_float_loc)
        a = self.find_element(*self._left_float_loc)
        href = a.get_attribute('href')
        css_prop = a.value_of_css_property('background')
        groups = self.css_url_pat.findall(css_prop)
        url = groups[0] if groups else None
        return href, url.replace('"', "")

    def get_right_float_links(self, no_phone=False):
        a = self.find_element(*self._right_float_a_loc)
        href = a.get_attribute('href')
        if no_phone:
            css_prop = a.value_of_css_property('background')
            groups = self.css_url_pat.findall(css_prop)
            url = groups[0] if groups else None
            link = url.replace('"', "")
        else:
            img = self.find_element(*self._right_float_img_loc)
            link = img.get_attribute('src')
        return href, link


