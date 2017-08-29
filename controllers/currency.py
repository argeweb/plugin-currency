#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
from argeweb import Controller, scaffold, route_menu


class Currency(Controller):
    class Scaffold:
        display_in_list = ['title', 'short_name', 'unit_name', 'exchange_rate', 'is_enable']
        hidden_in_form = ['is_main']

    @route_menu(list_name=u'system', group=u'金流管理', text=u'幣別設定', sort=894)
    def admin_list(self):
        main = self.meta.Model.get_or_create_main_currency()
        return scaffold.list(self)