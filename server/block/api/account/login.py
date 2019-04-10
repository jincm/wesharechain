#coding:utf-8

from tornado.web import RequestHandler
import time
from util.exception import ParamExist
from util import common_util
import logging
import json
from operation import user

LOG = logging.getLogger(__name__)

class LoginHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def post(self):
        try:
            phone = self.get_argument('phone', '')
            verify_code = self.get_argument('verify_code', '')
            #验证下手机验证码

            op = user.UserOp()
            _ = op.login(phone)
            token = common_util.gen_token(_.get("id"), int(time.time()))
            self.finish(json.dumps({
                'state': 0,
                'message': 'ok',
                'user_info': _,
                'token': token
            }))
        except Exception as ex:
            LOG.error("Reset pwd error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Login error'}))