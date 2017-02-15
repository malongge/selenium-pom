from .base_page import BasePage
from .page import Page
from selenium.webdriver.common.by import By


class LogoutPage(BasePage):

    @property
    def header(self):
        return self.Header(self.base_url, self.selenium)

    class Header(Page):
        _login_form_locator = (By.CSS_SELECTOR, '.nav_login a')

        @property
        def is_user_not_login(self):
            return self.is_element_present(*self._login_form_locator)

