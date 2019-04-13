#coding:utf-8

from tornado.web import RequestHandler
import time
from util.exception import ParamExist
from util import common_util
import logging
import json
from operation import user
from operation import verify_manage

LOG = logging.getLogger(__name__)

class LoginHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def post(self):
        try:
            phone = self.get_argument('phone', '')
            verify_code = self.get_argument('verify_code', '')

            op = user.UserOp()
            # 验证下手机
            filters = {
                "phone": phone
            }
            user_list = op.lists(**filters)
            if not user_list:
                self.finish(json.dumps({'state': 2, "message": "User phone not register"}))
                return

            # 验证验证码
            code_op = verify_manage.VerifyOp()
            # code_list = code_op.lists(**filters)
            # if code_list:
            #     code_info = code_op.views(code_list[0])
            #
            # if verify_code != code_info.get('verify_code', ''):
            #     self.finish(json.dumps({'state': 3, "message": "Verify code not equl"}))
            #     return
            verify_re = code_op.verify_code_phone(phone=phone, code=verify_code)
            if not verify_re:
                self.finish(json.dumps({'state': 1, "message": "Verify code failed"}))
                return

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