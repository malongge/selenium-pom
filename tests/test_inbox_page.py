#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Created by malongge on 2017/2/16 
#

import pytest

from .base import BaseTest
from pages.inbox_page import InboxPage


class TestInboxPage(BaseTest):

    def test_inbox_layer_once(self, base_url, selenium, login):
        """检查弹出的拦截层是否出现"""
        ulg, home_pg = login
        home_pg.close_ad_intercept()
        home_pg.click_inbox()
        inbox = InboxPage(base_url, selenium)
        inbox.check_inbox_layer()



