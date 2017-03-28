#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


def get_current_currency_exchange_rate(*args, **kwargs):
    controller = kwargs['controller']
    use_currency_name = ''
    if 'use_currency' in controller.session:
        use_currency_name = controller.session['use_currency']
    if 'use_currency' in kwargs:
        use_currency_name = kwargs['use_currency']
    if use_currency_name is '':
        use_currency_name = 'main'
    return CurrencyModel.get_current_or_main_currency(use_currency_name)


class CurrencyModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'幣值名稱')
    short_name = Fields.StringProperty(verbose_name=u'簡短的名稱', default=u'')
    unit_name = Fields.StringProperty(verbose_name=u'單位名稱', default=u'元')
    exchange_rate = Fields.FloatProperty(verbose_name=u'匯率', default=1.0)
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'顯示於前台')
    is_main = Fields.BooleanProperty(default=False, verbose_name=u'是否為基準貨幣')

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        return cls.query(cls.is_enable==True).order(-cls.sort)

    @classmethod
    def get_or_create_main_currency(cls):
        main = cls.find_by_name('main')
        if main is None:
            main = cls()
            main.name = 'main'
            main.is_main = True
            main.title = '基準貨幣'
            main.short_name = u'Main'
            main.unit_name = u'元'
            main.is_enable = False
            main.exchange_rate = 1
            main.put()
        return main

    @classmethod
    def get_current_or_main_currency(cls, currency_name):
        current_currency = cls.find_by_name(currency_name)
        if current_currency is None:
            current_currency = CurrencyModel.get_or_create_main_currency()
        return current_currency

    @classmethod
    def get_current_or_main_currency_with_controller(cls, controller):
        use_currency_name = ''
        if 'use_currency' in controller.session:
            use_currency_name = controller.session['use_currency']
        if use_currency_name is '':
            use_currency_name = 'main'
        return cls.get_current_or_main_currency(use_currency_name)

    def calc(self, target, places=2):
        if self.exchange_rate == 0:
            target = 0.0
        if target == u'':
            target = 0.0
        n = 10.0 ** places
        try:
            f_target = float(target)
            if f_target == 0:
                return 0
            target = f_target / float(self.exchange_rate)
        except:
            target = 0.0
        return int(target * n) / n * 1.0
