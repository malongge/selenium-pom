from selenium.webdriver.common.by import By

from .login_page import _LoginPage


class HomePage(_LoginPage):
    _page_title = "我的佳缘_世纪佳缘交友网"

    # 元素定位
    _inbox_loc = (By.CSS_SELECTOR, '.cp-menu-card-mail .menu-left')
    _login_layer_ad_loc = (By.ID, 'usercp_dltc_div')

    def home_page_and_close_layer(self):
        """确定是我的佳缘主页， 如果不是进行导航跳转"""

        if self.is_the_current_page:
            pass
        else:
            self.nav_to_home_page()
        # 跳转后，确认 title 没有问题
        assert self.is_the_current_page
        self.close_ad_intercept()

    def click_inbox(self):
        self.wait_for_element_to_be_visible(*self._inbox_loc)
        inbox = self.find_element(*self._inbox_loc)
        inbox.click()
        
    def check_login_layer(self):
        with self.focus_frame(self._login_layer_frame_loc):
            self.wait_for_element_present(*self._login_layer_ad_loc)
            assert self.find_element(*self._login_layer_ad_loc)





class NoPhoneHomePage(HomePage):
    _left_float_loc = (By.ID, "jyfc_yx_left_a")

    def get_left_float_links(self):
        self.wait_for_element_to_be_visible(*self._left_float_loc)
        a = self.find_element(*self._left_float_loc)
        href = a.get_attribute('href')
        css_prop = a.value_of_css_property('background')
        groups = self.css_url_pat.findall(css_prop)
        url = groups[0] if groups else None
        return href, url.replace('"', "")
