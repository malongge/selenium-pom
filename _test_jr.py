from pages.jr_page import JRPage


class TestJRPage(object):
    def test_zero_buy(self, base_url, selenium, existing_user):
        jr_pg = JRPage(base_url, selenium)
        jr_pg.get_relative_path('/showhome/index?f=1')
        jr_pg.click_zero_buy()
