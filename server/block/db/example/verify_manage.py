#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models
from db import api

class VerifyDB(Base):
    def __init__(self):
        super(VerifyDB, self).__init__()
        self.model = models.VerifyManage

    def update_by_phone(self, phone, **kwargs):
        query = api.model_query(self.model).filter_by(phone=phone)
        result = query.update(kwargs)
        if not result:
            return None
        return result

    def verify_manage_get_by_phone(self, phone):
        query = api.model_query(self.model).filter_by(phone=phone)
        result = query.first()
        if not result:
            return None
        return result

