#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
from datetime import datetime
from argeweb import Controller, scaffold, route_menu, route_with, route, settings
from argeweb import auth, add_authorizations
from argeweb.components.pagination import Pagination
from argeweb.components.csrf import CSRF, csrf_protect
from argeweb.components.search import Search
from plugins.mail import Mail
from ..models.currency_model import CurrencyModel


class Data(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search, CSRF)
        pagination_actions = ('list',)
        pagination_limit = 50
        default_view = 'json'
        Model = CurrencyModel

    @route
    @route_with('/data/currency/items', name='data:currency:items')
    def items(self):
        self.meta.change_view('json')
        n_data = []
        data = self.meta.Model.all_enable().fetch(1000)
        use_currency_name = ''
        if 'use_currency' in self.session:
            use_currency_name = self.session['use_currency']
        main_currency_record = self.meta.Model.find_by_name('main')
        main_currency = None
        current_currency = None
        for item in data:
            currency_item = {
                'key': self.util.encode_key(item),
                'sort': item.sort,
                'title': item.title,
                'name': item.name,
                'short_name': item.short_name,
                'unit_name': item.unit_name,
                'exchange_rate': item.exchange_rate,
                'is_enable': item.is_enable,
                'is_main': item.is_main,
                'is_current': False
            }
            n_data.append(currency_item)
            if item.is_main:
                main_currency = currency_item
            if item.name == use_currency_name:
                current_currency = currency_item
        if main_currency is None:
            main_currency = {
                'key': self.util.encode_key(main_currency_record),
                'sort': main_currency_record.sort,
                'title': main_currency_record.title,
                'name': main_currency_record.name,
                'short_name': main_currency_record.short_name,
                'unit_name': main_currency_record.unit_name,
                'exchange_rate': main_currency_record.exchange_rate,
                'is_enable': main_currency_record.is_enable,
                'is_main': main_currency_record.is_main,
                'is_current': False
            }
        if main_currency == current_currency or current_currency is None:
            main_currency['is_current'] = True
            current_currency = main_currency
        else:
            current_currency['is_current'] = True
        self.context['data'] = {
            'main': main_currency,
            'current': current_currency,
            'items': n_data
        }