#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Created by malongge on 2017/2/16 
#

import time

import pytest

from .base import BaseTest
class TestHomePage(BaseTest):

    @pytest.mark.flaky(reruns=3)
    def test_home_focus_pic_auto_run(self, login):

        _, pg = login
        pg.click_index_link()
        pg.switch_to_second_window()
        link1 = pg.get_focus_pic_img_link()
        time.sleep(4)
        link2 = pg.get_focus_pic_img_link()
        time.sleep(4)
        link3 = pg.get_focus_pic_img_link()
        time.sleep(4)
        link4 = pg.get_focus_pic_img_link()
        assert link1 != link2 != link3 != link4, '轮播图应该每个 4s 会有轮播， 但未检测到有自动轮播'

    @pytest.mark.flaky(reruns=3)
    def test_home_hover_focus_pic_btn(self, login):
        index_pg, home_pg = login
        home_pg.click_index_link()
        time.sleep(1)
        home_pg.switch_to_second_window()
        btns = index_pg.get_focus_pic_hover_buttons()
        index_pg.hover(btns[0])
        link1 = index_pg.get_focus_pic_link()
        img1 = index_pg.get_focus_pic_img_link()
        assert self._check_link_request_code(img1), '第一张轮播图：{} 不显示'.format(img1)
        assert self._check_link_request_code(link1), '第一张轮播图链接地址:{}, 打不开'.format(link1)
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