import time

import pytest

from pages.home_page import HomePage
from pages.index_page import IndexPage
from pages.logout_page import LogoutPage
from .base import BaseRecordTest


class TestIndexPage(BaseRecordTest):
    @pytest.mark.flaky(reruns=3)
    def test_login_and_logout(self, base_url, selenium, existing_user):
        index_pg = IndexPage(base_url, selenium)
        home_pg = HomePage(base_url, selenium)
        logout_pg = LogoutPage(base_url, selenium)
        index_pg.get_relative_path('/')
        time.sleep(1)
        assert index_pg.header.is_user_not_login, '刚开始网页是没有登录， 但检测为登录了'
        index_pg.header.login(existing_user['username'], existing_user['password'])
        assert home_pg.header.is_user_logged_in, '登录完后应该是进入登录状态， 但依然为未登录状态'
        time.sleep(3)
        home_pg.close_ad_intercept()
        home_pg.header.click_logout()
        assert logout_pg.header.is_user_not_login

    @pytest.mark.flaky(reruns=3)
    def test_focus_pic_auto_run(self, base_url, selenium, uid_cookie):
        index_pg = IndexPage(base_url, selenium)
        index_pg.get_cookie_index_page('/', uid_cookie)
        link1 = index_pg.get_focus_pic_img_link()
        time.sleep(4)
        link2 = index_pg.get_focus_pic_img_link()
        time.sleep(4)
        link3 = index_pg.get_focus_pic_img_link()
        assert link1 != link2 != link3, '轮播图应该每个 4s 会有轮播， 但未检测到有自动轮播'

    @pytest.mark.flaky(reruns=3)
    def test_hover_focus_pic_btn(self, base_url, selenium, uid_cookie):
        index_pg = IndexPage(base_url, selenium)
        index_pg.get_cookie_index_page('/', uid_cookie)
        btns = index_pg.get_focus_pic_hover_buttons()
        index_pg.hover(btns[0])
        img1 = index_pg.get_focus_pic_img_link()
        assert self._check_link_request_code(img1), '第一张轮播图：{} 不显示'.format(img1)
        index_pg.hover(btns[1])
        link2 = index_pg.get_focus_pic_link()
        img2 = index_pg.get_focus_pic_img_link()
        assert self._check_link_request_code(img2), '第二张轮播图：{} 不显示'.format(img2)
        assert self._check_link_request_code(link2), '第二张轮播图链接地址:{}, 打不开'.format(link2)
        index_pg.hover(btns[2])
        link3 = index_pg.get_focus_pic_link()
        img3 = index_pg.get_focus_pic_img_link()
        assert self._check_link_request_code(img3), '第三张轮播图：{} 不显示'.format(img3)
        assert self._check_link_request_code(link3), '第三张轮播图链接地址:{}, 打不开'.format(link3)
        assert img1 != img2 != img3, '轮播图应该在鼠标放到轮播按钮时进行切换， 但未检测到切换'
