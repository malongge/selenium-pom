from .page import Page


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



