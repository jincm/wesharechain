
#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
from util.convert import is_user_name, is_mobile, bs2utf8
import logging
import json
from operation import user

LOG = logging.getLogger(__name__)

class UserHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        pass

    def post(self):
        try:
            phone = bs2utf8(self.get_argument('phone', ''))
            verify_code = self.get_argument('verify_code', '')
            invitation = self.get_argument('invitation', '')
            if not is_mobile(phone):
                self.finish(json.dumps({'state': 3, "message": "User phone format error"}))
                return

            #验证手机是否已经被注册
            #验证验证码

            #验证邀请码，并通过邀请码获取邀请用户
            referrer_id = "" #邀请人用户id
            op = user.UserOp()
            op.create(phone=phone, referrer_id=referrer_id)
            self.finish(json.dumps({'state': 0, "message": "sing in succes"}))
        except ParamExist as ex:
            LOG.error("Sign error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("Sign error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'account sign error'}))

    def put(self, *args, **kwargs):
        pass
