#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Created by malongge on 2017/2/16 
#

import pytest

from pages.home_page import HomePage
from pages.index_page import IndexPage
from .base import BaseTest


class TestHomePage(BaseTest):
    def _check_right_float(self, home_pg, base_info, no_phone=False):
        href, link = home_pg.get_right_float_links(no_phone=no_phone)
        assert href is not None, base_info + "链接地址应该存在"
        assert link is not None, base_info + "应该有图片"

        assert self._check_link_request_code(href), base_info + "链接地址访问链接不存在或者有问题"
        assert self._check_link_request_code(link), base_info + "图片没有显示"

    def _check_left_float(self, home_pg, base_info):
        href, link = home_pg.get_left_float_links()
        assert href is not None, base_info + "链接地址应该存在"
        assert link is not None, base_info + "应该有图片"

        assert self._check_link_request_code(href), base_info + "链接地址访问链接不存在或者有问题"
        assert self._check_link_request_code(link), base_info + "图片没有显示"

    @pytest.mark.flaky(reruns=3)
    def test_home_left_float_show_with_phone_user(self, login):
        _, home_pg = login
        base_info = '登录首页左浮层，'

        self._check_left_float(home_pg, base_info)

    @pytest.mark.flaky(reruns=3)
    def test_home_right_float_show_with_phone_user(self, login):
        _, home_pg = login
        base_info = '认证用户登录后的右浮层，'
        self._check_right_float(home_pg, base_info)

    @pytest.mark.flaky(reruns=3)
    def test_float_with_nophone_user(self, base_url, selenium, nophone_user):
        login_pg = IndexPage(base_url, selenium)
        home_pg = HomePage(base_url, selenium)
        login_pg.get_relative_path('/')
        login_pg.maximize_window()
        login_pg.header.login(nophone_user['username'], nophone_user['password'])
        home_pg.close_nophone_ad_intercept()
        base_info = '非手机认证用户登录后的左浮层'
        self._check_left_float(home_pg, base_info)
        base_info = '非手机认证用户登录后的右浮层'
        self._check_right_float(home_pg, base_info, True)
