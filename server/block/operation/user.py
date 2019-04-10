#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.user import UserDB
from util.encrypt_md5 import encry_md5

class UserOp(Base):
    def __init__(self):
        super(UserOp, self).__init__()
        self.exampledb = UserDB()

    def login(self, name="", pwd="", phone=""):
        filters = {
            "pwd": encry_md5(pwd)
        }
        if name:
            filters.update({"name": name})
        elif phone:
            filters.update({"phone": phone})
        else:
            return

        user_list = self.lists(**filters)
        if user_list:
            user_info = self.views(user_list[0])
            return user_info

