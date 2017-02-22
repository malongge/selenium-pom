#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Created by malongge on 2017/2/16 
#

import pytest

from .base import BaseRecordTest


class TestHomePage(BaseRecordTest):
    @pytest.mark.flaky(reruns=3)
    def test_home_left_float_show_with_phone_user(self, login):
        _, home_pg = login
        href, link = home_pg.get_left_float_links()
        base_info = '登录首页左浮层，'
        assert href is not None, base_info + "链接地址应该存在"
        assert link is not None, base_info + "应该有图片"

        assert self._check_link_request_code(href), base_info + "链接地址访问链接不存在或者有问题"
        assert self._check_link_request_code(link), base_info + "图片没有显示"

    @pytest.mark.flaky(reruns=3)
    def test_home_right_float_show_with_phone_user(self, login):
        _, home_pg = login
        href, link = home_pg.get_right_float_links()
        base_info = '登录首页右浮层，'
        assert href is not None, base_info + "链接地址应该存在"
        assert link is not None, base_info + "应该有图片"

        assert self._check_link_request_code(href), base_info + "链接地址访问链接不存在或者有问题"
        assert self._check_link_request_code(link), base_info + "图片没有显示"
