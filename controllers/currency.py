#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
import random
from argeweb import Controller, scaffold, route_menu, Fields, route_with
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search


class Currency(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)
        pagination_limit = 50

    class Scaffold:
        display_in_list = ('title', 'short_name', 'unit_name', 'exchange_rate', 'is_enable')
        hidden_in_form = ('is_main')

    @route_menu(list_name=u'backend', text=u'幣值設定', sort=9934, group=u'系統設定')
    def admin_list(self):
        main = self.meta.Model.get_or_create_main_currency()
        return scaffold.list(self)