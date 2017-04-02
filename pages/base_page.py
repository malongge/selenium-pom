from .page import Page

from selenium.webdriver.common.by import By

class BasePage(Page):
    def get_cookie_index_page(self, url, cookie):
        self.get_relative_path(url)
        self.maximize_window()
        self.selenium.add_cookie(cookie)
        self.selenium.refresh()

    def switch_to_second_window(self):
        handles = self.selenium.window_handles
        try:
            handle = handles[1]
        except IndexError:
            handle = handles[0]
        self.selenium.switch_to_window(handle)

    def get_img_link(self, img_element):
        elem = self.find_element(*img_element)
        return elem.get_attribute('src')

    def get_a_href_link(self, a_element):
        elem = self.find_element(*a_element)
        return elem.get_attribute('href')

    def get_a_and_img_links(self, atag_element):
        # selector, a = atag_element
        # assert selector == By.CSS_SELECTOR
        # img = a + ' img'
        # a_elem = self.find_element(selector, a)
        # img_elem = self.find_element(selector, img)
        # return a_elem.get_attribute('href'), img_elem.get_attribute('src')
        a_elem = self.find_element(*atag_element)
        img_elem = a_elem.find_element(By.TAG_NAME, 'img')
        return a_elem.get_attribute('href'), img_elem.get_attribute('src')



