#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models

class OrderDB(Base):
    def __init__(self):
        super(OrderDB, self).__init__()
        self.model = models.OrderInfo