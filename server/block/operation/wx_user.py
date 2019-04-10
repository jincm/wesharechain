#!/usr/bin/python
# -*- coding: utf-8 -*-
from operation import Base
from db.example.wx_user import WxUserDB
from db.example.user import UserDB

class WxUserOp(Base):
    def __init__(self):
        self.exampledb = WxUserDB()

    def create(self, **kwargs):
        user_values = {
            "nick_name": kwargs.get("wx_name"),
            "phone": kwargs.get("phone"),
        }
        if kwargs.get("referrer_id", ""):
            user_values.update({"referrer_id": kwargs.get("referrer_id")})
        userdb = UserDB()
        user_info = userdb.create(**user_values)

        wx_values={
            "user_id": user_info.get("id"),
            "code": kwargs.get("code"),
            "openid": kwargs.get("openid"),
            "session_key": kwargs.get("session_key"),
            "wx_name": kwargs.get("wx_name")
        }
        wx_userInfo = self.exampledb.create(**wx_values)
        return wx_userInfo


    def info_by_openid(self, openid):
        _ = self.lists(openid=openid)
        if _:
            return self.views(_[0])
