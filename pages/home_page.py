from .base_page import BasePage
from .page import Page
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    _ad_intercept_close_loc = (By.CSS_SELECTOR, '#usercp_dltc_div a')
    _login_layer_frame_loc = (By.ID, 'login_layer')
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

