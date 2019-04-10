#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.verify_manage import VerifyDB

class VerifyOp(Base):
    def __init__(self):
        super(VerifyOp, self).__init__()
        self.exampledb = VerifyDB()