from selenium.webdriver.common.by import By

from .login_page import _LoginPage


class InboxPage(_LoginPage):
    _page_title = "收件箱_世纪佳缘交友网"

    # 元素定位
    _inbox_frame_loc = (By.ID, 'iframe_content2')
    _mail_ad_layer_loc = (By.CSS_SELECTOR, '.mail_layer')
    _mail_ad_layer_close_loc = (By.CSS_SELECTOR, '.mail_layer .mail_layerClose')

    _vip_top_ad_loc = (By.ID, 'ad_pos_pcweb_67')

    def check_inbox_layer(self):
        with self.focus_frame(self._inbox_frame_loc):
            self.wait_for_element_present(*self._mail_ad_layer_loc)
            assert self.find_element(*self._mail_ad_layer_loc)

    def close_mail_ad_layer(self):
        with self.focus_frame(self._inbox_frame_loc):
            self.wait_for_element_present(*self._mail_ad_layer_loc)
            close_link = self.find_element(*self._mail_ad_layer_close_loc)
            close_link.close()

    def check_vip_ad_exist(self):
        assert self.find_element(*self._vip_top_ad_loc)





