#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.order import OrderDB

class OrderOp(Base):
    def __init__(self):
        super(OrderOp, self).__init__()
        self.exampledb = OrderDB()

    def create(self,  commodity_code='', order_type='', original_price='', real_price=''):
        kwargs = {
            'commodity_code': commodity_code,
            'order_type': order_type,
            'original_price':  float(original_price),
            'real_price': float(real_price)
        }
        return self.exampledb.create(**kwargs)

    def update(self, id='', status=''):
        kwargs = {'status': status}
        return self.exampledb.update(id, **kwargs)

    def lists(self, offset=0, limit=1000, id='', order_type='', status='', **kwargs):
        filters = {
            'offset': offset,
            'limit': limit
        }
        if id:
            filters.update({"id": id})
        if order_type:
            filters.update({"order_type": order_type})
        if status:
            filters.update({"status": status})

        order_list = self.exampledb.lists(offset, limit, **filters)
        return order_list
