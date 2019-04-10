#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.commodity import CommodityDB

class CommodityOp(Base):
    def __init__(self):
        super(CommodityOp, self).__init__()
        self.exampledb = CommodityDB()