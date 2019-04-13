#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.commodity import CommodityDB

class CommodityOp(Base):
    def __init__(self):
        super(CommodityOp, self).__init__()
        self.exampledb = CommodityDB()

    def create(self,  name='', describe='', original_price='', real_price='', commodity_type='', file_path='', **kwargs):
        kwargs = {
            'name': name,
            'describe': describe,
            'original_price': float(original_price),
            'real_price': float(real_price),
            'commodity_type': commodity_type,
            'file_path': file_path
        }
        self.exampledb.create(**kwargs)

    def update(self, id='', name='', describe='', original_price='', real_price='', commodity_type='', file_path='', **kwargs):
        kwargs = {
            'name': name,
            'describe': describe,
            'original_price': float(original_price),
            'real_price': float(real_price),
            'commodity_type': commodity_type,
            'file_path': file_path
        }
        self.exampledb.update(id, **kwargs)

    def lists(self, offset=0, limit=1000, id='', name='', **kwargs):
        filters = {
            'offset': offset,
            'limit': limit
        }
        if id:
            filters.update({"id": id})
        if name:
            filters.update({"name": name})

        order_list = self.exampledb.lists(offset, limit, **filters)
        return order_list
