import time

from selenium.webdriver.common.by import By

from .login_page import _LoginPage


class IndexPage(_LoginPage):
    _page_title = "世纪佳缘交友网：国内领先的在线婚恋交友网站，免费注册马上寻缘"

    # 轮播图元素
    _focus_pic_loc = (By.CSS_SELECTOR, '#flash_id1 a')
    _focus_pic_img_loc = (By.CSS_SELECTOR, '#flash_id1 a img')
    _focus_pic_btn_loc = (By.CSS_SELECTOR, '#flash_id1_1 a')

    index_url = 'http://www.jiayuan.com/'

    _wait_for_visible_loc = (By.CSS_SELECTOR, '.flash')

    def get_focus_pic_link(self):
        elem = self.find_element(*self._focus_pic_loc)
        return elem.get_attribute('href')

    def get_focus_pic_img_link(self):
        self.wait_for_element_to_be_visible(*self._focus_pic_img_loc)
        elem = self.find_element(*self._focus_pic_img_loc)
        return elem.get_attribute('src')

    def get_focus_pic_hover_buttons(self):
        return self.find_elements(*self._focus_pic_btn_loc)

    def switch_to_index_page(self, home_page):
        if self.is_the_current_page:
            pass
        else:
            home_page.close_ad_intercept()
            home_page.nav_to_page(self.index_url)
            time.sleep(3)
            self.switch_to_second_window()
            self.wait_for_element_to_be_visible(*self._wait_for_visible_loc)







