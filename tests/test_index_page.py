import time

import pytest
from pages.index_page import IndexPage
from .base import BaseTest


class TestIndexPage(BaseTest):
    @pytest.mark.flaky(reruns=1)
    def test_index_focus_pic_auto_run(self, base_url, selenium, login):
        _, pg = login
        index_pg = IndexPage(base_url, selenium)
        index_pg.switch_to_index_page(pg)
        # 根据按钮的数量来确定轮播图的数量
        btns = index_pg.get_focus_pic_hover_buttons()
        assert len(btns) > 1

        # 轮播图每 4s 进行切换， 注意在执行的时候，鼠标不要放到轮播图上， 否则会影响测试结果
        links = []
        for _ in btns:
            link = index_pg.get_focus_pic_img_link()
            links.append(link)
            time.sleep(4)

        for index, value in enumerate(links[:-1]):
            assert links[index] != links[index + 1], '轮播第 {} 张链接地址为 {} 应该在 4s 后轮播， 但未检测到有轮播'.format(index, value)


    @pytest.mark.flaky(reruns=1)
    def test_index_hover_focus_pic_btn(self, base_url, selenium, login):
        _, pg = login
        index_pg = IndexPage(base_url, selenium)
        index_pg.switch_to_index_page(pg)
        # 根据按钮的数量来确定轮播图的数量
        btns = index_pg.get_focus_pic_hover_buttons()
        assert len(btns) > 1

        img_links = []
        for index, btn in enumerate(btns):
            index_pg.hover(btn)
            img = index_pg.get_focus_pic_img_link()
            assert self._check_link_request_code(img, index_pg), '第 {} 张轮播图：{} 不显示'.format(index, img)
            link = index_pg.get_focus_pic_link()
            assert self._check_link_request_code(link, index_pg), '第 {} 张轮播图的链接 {} 请求状态码非 200'.format(index, img)
            img_links.append(img)

        for index in range(0, len(img_links) - 1):
            assert img_links[index] != img_links[index + 1], '轮播图应该在鼠标放到轮播 {} 按钮时进行切换， 但未检测到切换'.format(index + 1)
