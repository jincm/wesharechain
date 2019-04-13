#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.verify_manage import VerifyDB
from datetime import datetime
from util import convert
import logging

LOG = logging.getLogger(__name__)


class VerifyOp(Base):
    def __init__(self):
        super(VerifyOp, self).__init__()
        self.exampledb = VerifyDB()

    def update_by_phone(self, phone, **kwargs):
        self.exampledb.update_by_phone(phone, **kwargs)

    def exist(self, filters):
        if self.lists(**filters):
            return True
        else:
            return False

    def verify_code_phone(self, phone="", code=""):
        verify_info = self.exampledb.verify_manage_get_by_phone(phone)
        if verify_info:
            _now = datetime.now()
            if convert.bs2utf8(verify_info.verify_code) == code and verify_info.update_time:
                _ = (_now - verify_info.update_time).seconds
                LOG.info("verify code time:%d" % _)
                if _ < 15 * 60:
                    return True

        return False