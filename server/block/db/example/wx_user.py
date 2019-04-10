#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models

class WxUserDB(Base):
    def __init__(self):
        self.model = models.WxUserinfo