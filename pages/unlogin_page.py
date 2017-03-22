from selenium.webdriver.common.by import By

from .base_page import BasePage
from .page import Page


class UnloginPage(BasePage):
    page_title = ""


    # 轮播图元素
    _focus_pic_loc = (By.CSS_SELECTOR, '#flash_id1 a')
    _focus_pic_img_loc = (By.CSS_SELECTOR, '#flash_id1 a img')
    _focus_pic_btn_loc = (By.CSS_SELECTOR, '#flash_id1_1 a')

    def get_focus_pic_link(self):
        elem = self.find_element(*self._focus_pic_loc)
        return elem.get_attribute('href')

    def get_focus_pic_img_link(self):
        elem = self.find_element(*self._focus_pic_img_loc)
        return elem.get_attribute('src')

    def get_focus_pic_hover_buttons(self):
        return self.find_elements(*self._focus_pic_btn_loc)

    @property
    def header(self):
        return self.Header(self.base_url, self.selenium)

    class Header(Page):
        _login_form_locator = (By.ID, 'hder_login_form_new')
        _username_input_locator = (By.CSS_SELECTOR, "#hder_login_form_new > input[name='name']")
        _passwrod_input_locator = (By.CSS_SELECTOR, "#hder_login_form_new > input[name='password']")
        _submit_locator = (By.CSS_SELECTOR, "button.btn_login.sprite")
        _logout_locator = (By.CSS_SELECTOR, '#head_user_logout a')
        _user_name_locator = (By.CSS_SELECTOR, '#head_user_nickname a')

        def enter_password(self, value):
            password = self.find_element(*self._passwrod_input_locator)
            password.clear()
            password.send_keys(value)

        def enter_username(self, value):
            username = self.find_element(*self._username_input_locator)
            username.clear()
            username.send_keys(value)

        def login(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            self.find_element(*self._submit_locator).click()

        @property
        def is_user_not_login(self):
            return self.is_element_present(*self._login_form_locator)

