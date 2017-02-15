from .page import Page
from selenium.webdriver.common.by import By


class JRPage(Page):
    zero_buy_loc = (By.CSS_SELECTOR, "a[href='/zeroBuy']")

    def click_zero_buy(self):
        self.find_element(*self.zero_buy_loc).click()
