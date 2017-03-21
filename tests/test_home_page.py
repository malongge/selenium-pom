#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Created by malongge on 2017/2/16 
#

import pytest

from .base import BaseTest


class TestHomePage(BaseTest):
    #
    # def set_up_01(self):
    #     pass

    def _check_right_float(self, home_pg, base_info, no_phone=False):
        href, link = home_pg.get_right_float_links(no_phone=no_phone)
        assert href is not None, base_info + "链接地址应该存在"
        assert link is not None, base_info + "应该有图片"

        assert self._check_link_request_code(href, home_pg), base_info + "链接地址访问链接不存在或者有问题"
        assert self._check_link_request_code(link, home_pg), base_info + "图片没有显示"

    def _check_left_float(self, home_pg, base_info):
        href, link = home_pg.get_left_float_links()
        assert href is not None, base_info + "链接地址应该存在"
        assert link is not None, base_info + "应该有图片"
        assert self._check_link_request_code(link, home_pg), base_info + "图片 {} 没有显示".format(link)
        assert self._check_link_request_code(href, home_pg), base_info + "图片没有显示"

    @pytest.mark.flaky(reruns=1)
    def test_float_show_with_phone_user(self, login):
        ulg, home_pg = login
        home_pg.home_page_and_close_layer()
        base_info = '登录首页左浮层，'
        self._check_left_float(home_pg, base_info)

    @pytest.mark.flaky(reruns=1)
    def test_float_with_nophone_user(self, nophone_login):
        ulg, home_pg = nophone_login
        home_pg.home_page_and_close_layer()
        base_info = '非手机认证用户登录后的左浮层'
        self._check_left_float(home_pg, base_info)
        base_info = '非手机认证用户登录后的右浮层'
        self._check_right_float(home_pg, base_info, True)
