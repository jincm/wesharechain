#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.user import UserDB
from util.encrypt_md5 import encry_md5



class UserOp(Base):
    def __init__(self):
        super(UserOp, self).__init__()
        self.exampledb = UserDB()

    def login(self, phone, name=""):
        filters = {
            # "pwd": encry_md5(pwd)
            "phone": phone
        }
        if name:
            filters.update({"name": name})

        user_list = self.lists(**filters)
        if user_list:
            user_info = self.views(user_list[0])
            return user_info

    def exist(self, filters):
        user_list = self.lists(**filters)
        if user_list:
            return True
        else:
            return False
