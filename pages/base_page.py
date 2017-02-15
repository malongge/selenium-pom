from selenium.webdriver.common.by import By

from .page import Page


class BasePage(Page):
    def get_cookie_index_page(self, url, cookie):
        self.get_relative_path(url)
        self.selenium.add_cookie(cookie)
        self.selenium.refresh()
