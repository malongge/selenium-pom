import time

import pytest

from pages.home_page import HomePage
from pages.unlogin_page import UnloginPage
from pages.logout_page import LogoutPage
from .base import BaseTest


class TestUnloginPage(BaseTest):
    def test_login_and_logout(self, base_url, selenium, existing_user):
        ulg = UnloginPage(base_url, selenium)
        ig = HomePage(base_url, selenium)
        logout_pg = LogoutPage(base_url, selenium)
        ulg.get_relative_path('/')
        assert ulg.header.is_user_not_login, '刚开始网页是没有登录， 但检测为登录了'
        ulg.header.login(existing_user['username'], existing_user['password'])
        assert ig.header.is_user_logged_in, '登录完后用户 {} 应该是进入登录状态， 但依然为未登录状态'.format(existing_user)
        ig.close_ad_intercept()
        ig.header.click_logout()
        assert logout_pg.header.is_user_not_login

    @pytest.mark.flaky(reruns=2)
    def test_focus_pic_auto_run(self, base_url, selenium, uid_cookie):
        ulg = UnloginPage(base_url, selenium)
        ulg.get_cookie_index_page('/', uid_cookie)
        # 根据按钮的数量来确定轮播图的数量
        btns = ulg.get_focus_pic_hover_buttons()
        assert len(btns) > 1

        # 轮播图每 4s 进行切换， 注意在执行的时候，鼠标不要放到轮播图上， 否则会影响测试结果
        links = []
        for _ in btns:
            link = ulg.get_focus_pic_img_link()
            links.append(link)
            time.sleep(4)

        for index, value in enumerate(links[:-1]):
            assert links[index] != links[index + 1], '轮播第 {} 张链接地址为 {} 应该在 4s 后轮播， 但未检测到有轮播'.format(index, value)

    @pytest.mark.flaky(reruns=2)
    def test_hover_focus_pic_btn(self, base_url, selenium, uid_cookie):
        ulg = UnloginPage(base_url, selenium)
        # 注入 my_uid cookie, 有 cookie 和没有 cookie 的情况页面展示不一样
        ulg.get_cookie_index_page('/', uid_cookie)
        btns = ulg.get_focus_pic_hover_buttons()
        img_links = []
        for index, btn in enumerate(btns):
            ulg.hover(btn)
            img = ulg.get_focus_pic_img_link()
            assert self._check_link_request_code(img, ulg), '第 {} 张轮播图：{} 不显示'.format(index, img)
            link = ulg.get_focus_pic_link()
            assert self._check_link_request_code(link, ulg), '第 {} 张轮播图的链接 {} 请求状态码非 200'.format(index, img)
            img_links.append(img)

        for index in range(0, len(img_links) - 1):
            assert img_links[index] != img_links[index + 1], '轮播图应该在鼠标放到轮播 {} 按钮时进行切换， 但未检测到切换'.format(index + 1)
