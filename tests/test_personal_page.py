#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Created by malongge on 2017/2/16 
#

import pytest

from .base import BaseTest
from pages.personal_page import PersonalPage
import time
from pages.common import _login


class TestPersonalPage(BaseTest):

    @pytest.fixture(autouse=True)
    def _to_personal_page(self, base_url, selenium, existing_user):
        person_pg = PersonalPage(base_url, selenium)
        if not person_pg.exist_cookie():
            from pages.home_page import HomePage
            ulg, home_pg = _login(base_url, selenium, HomePage, existing_user)
            home_pg.close_ad_intercept()
            home_pg.header.click_uid()
            home_pg.switch_to_second_window()
            time.sleep(1)
            person_pg = PersonalPage(base_url, selenium)
            person_pg.dump_cookie()
            self.person_pg = person_pg

        else:
            person_pg.get_relative_path('/')
            person_pg.maximize_window()
            person_pg.load_cookie()
            person_pg.refresh()
            person_pg.header.click_uid()
            person_pg.switch_to_second_window()
            time.sleep(1)
            self.person_pg = person_pg

    def test_personal_pg_top_ad(self):
        person_pg = self.person_pg
        self._check_a_and_img(person_pg._right_top_ad_a_loc, person_pg, '11')

    def test_right_middle_recommend_service_ad(self, base_url, selenium, login):
        person_pg = self.person_pg
        links = person_pg.find_all_recommend_service_link()
        for index, link in enumerate(links):
            print(link, '---------------')
            assert self._check_link_request_code(link, person_pg), '{} 广告位第{}列， 无法打开广告链接'.format(72, index + 1)

    def test_my_description_right_hand_ad(self):
        person_pg = self.person_pg
        self._check_a_and_img(person_pg._self_description_right_hand_ad_loc, person_pg, '102')