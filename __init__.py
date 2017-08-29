#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/07/08.

from argeweb import ViewDatastore, ViewFunction
from models.currency_model import CurrencyModel, get_current_currency_exchange_rate

ViewDatastore.register('currency_list', CurrencyModel.all_enable)
ViewDatastore.register('currency', CurrencyModel.get_by_name)
ViewFunction.register(get_current_currency_exchange_rate)

plugins_helper = {
    'title': u'幣別設定',
    'desc': u'幣別設定',
    'controllers': {
        'currency': {
            'group': u'幣別設定',
            'actions': [
                {'action': 'list', 'name': u'幣別設定'},
                {'action': 'add', 'name': u'新增幣別設定'},
                {'action': 'edit', 'name': u'編輯幣別設定'},
                {'action': 'view', 'name': u'檢視幣別設定'},
                {'action': 'delete', 'name': u'刪除幣別設定'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        }
    }
}