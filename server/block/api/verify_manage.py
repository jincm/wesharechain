#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
import logging
import json, datetime
from util.convert import bs2utf8, is_mobile
from util.common_util import create_verifycode, send_vrifycode
from operation import verify_manage


LOG = logging.getLogger(__name__)


class SendVerifyCodeHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def post(self):
        try:
            phone = bs2utf8(self.get_argument('phone', ''))
            if not phone:
                LOG.error("Not receive phone")
                self.finish(json.dumps({'state': 1, 'message': 'Not receive phone'}))
                return

            if not is_mobile(phone):
                LOG.error("User phone[%s,type:%s] format error" % (phone, type(phone)))
                self.finish(json.dumps({'state': 2, "message": "User phone format error"}))
                return

            verify_code = create_verifycode()

            # 存储验证码
            op = verify_manage.VerifyOp()
            # dt = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            filters = {
                "phone": phone
            }
            # 如果手机存在的更新
            if op.exist(filters):
                op.update_by_phone(phone, verify_code=verify_code)
            else:
                op.create(phone=phone, verify_code=verify_code)

            # 发送验证码给网关,并存储
            """
            send_re = send_vrifycode(verify_code)  # 返回的是json格式的
            LOG.info("Send verify code result:%s" % send_re)
            if send_re['status'] != 'success':
                self.finish(json.dumps({'state': 3, "message": "Send message error"}))
                return
"""
            self.finish(json.dumps({'state': 0, "message": "Send message success"}))
        except ParamExist as ex:
            LOG.error("order create error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'order create error'}))


