#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models

class VerifyDB(Base):
    def __init__(self):
        super(VerifyDB, self).__init__()
        self.model = models.VerifyManage