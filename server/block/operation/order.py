#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.order import OrderDB

class OrderOp(Base):
    def __init__(self):
        super(OrderOp, self).__init__()
        self.exampledb = OrderDB()