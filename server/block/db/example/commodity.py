#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models

class CommodityDB(Base):
    def __init__(self):
        super(CommodityDB, self).__init__()
        self.model = models.CommodityInfo