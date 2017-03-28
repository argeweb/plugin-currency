#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/1.
from random import randint
from datetime import datetime
from argeweb import Controller, scaffold, route_menu, route_with, route, settings
from argeweb import auth, add_authorizations
from argeweb.components.pagination import Pagination
from argeweb.components.csrf import CSRF, csrf_protect
from argeweb.components.search import Search
from plugins.mail import Mail
from plugins.user_shop_point.models.user_shop_point_model import UserShopPointModel
from plugins.shopping_cart.models.shopping_cart_item_model import ShoppingCartItemModel
from plugins.user_contact_data.models.user_contact_data_model import UserContactDataModel
from ..models.currency_model import CurrencyModel


class Form(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search, CSRF)
        default_view = 'json'
        Model = CurrencyModel

    @route
    @add_authorizations(auth.check_user)
    @route_with(name='form:currency:change')
    def change(self):
        item = self.meta.Model.find_by_name(self.params.get_string('currency', 'main'))
        if item is not None:
            self.session['use_currency'] = item.name
        self.context['data'] = {'result': 'success', 'currency': self.util.encode_key(item)}
        self.context['message'] = u'已成功更變。'