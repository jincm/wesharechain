
#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
from util.convert import is_user_name, is_mobile, bs2utf8
import logging
import json
from operation import user
from operation import verify_manage
from util import common_util
import time


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
                self.finish(json.dumps({'state': 2, "message": "User phone format error"}))
                return

            user_op = user.UserOp()

            # 验证手机是否已经被注册
            filters = {
                "phone": phone
            }
            # user_list = user_op.exist(filters)
            if user_op.exist(filters):
                self.finish(json.dumps({'state': 3, "message": "User phone registered"}))
                return

            # 验证验证码
            code_op = verify_manage.VerifyOp()
            # code_list = code_op.lists(**filters)
            # if code_list:
            #     code_info = code_op.views(code_list[0])
            #
            # if verify_code != code_info.get('verify_code', ''):
            #     self.finish(json.dumps({'state': 1, "message": "Verify code not equl"}))
            #     return
            verify_re = code_op.verify_code_phone(phone=phone, code=verify_code)
            if not verify_re:
                self.finish(json.dumps({'state': 1, "message": "Verify code failed"}))
                return

            # 验证邀请码，并通过邀请码获取邀请用户
            filters = {
                "invitation": invitation
            }
            user_list = user_op.lists(**filters)
            if not user_list:
                self.finish(json.dumps({'state': 4, "message": "Not found invated user"}))
                return

            user_info = user_op.views(user_list[0])
            referrer_id = user_info.get('id', '')  # 邀请人用户id

            user_op.create(phone=phone, referrer_id=referrer_id)

            self.finish(json.dumps({'state': 0, "message": "sing in succes"}))
        except ParamExist as ex:
            LOG.error("Sign error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("Sign error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'account sign error'}))

    def put(self, *args, **kwargs):
        try:
            id = self.get_argument('id', '')
            nick_name = self.get_argument('nick_name', None)
            sex = self.get_argument('sex', None)
            birthday = self.get_argument('birthday', None)
            phone = bs2utf8(self.get_argument('phone', None))
            token = self.get_argument('token', None)

            user_op = user.UserOp()

            if not id:
                LOG.error("Cannot update user info")
                self.finish(json.dumps({'state': 1, "message": "Cannot update user info"}))
                return

            update_dict = {}
            # _ = user_op.login(phone)
            # ser_token = common_util.gen_token(_.get("id"), int(time.time()))
            # if ser_token != token:
            #     self.finish(json.dumps({'state': 10, 'message': 'account sign error'}))
            if phone is not None:
                if not is_mobile(phone):
                    self.finish(json.dumps({'state': 1, "message": "User phone format error"}))
                    return

                filters = {
                    "phone": phone
                }
                if user_op.exist(filters):
                    self.finish(json.dumps({'state': 2, "message": "User phone registered"}))
                    return

                update_dict['phone'] = phone

            if nick_name is not None:
                if not is_user_name(nick_name):
                    self.finish(json.dumps({'state': 3, "message": "User name format error"}))
                    return
                update_dict['nick_name'] = nick_name

            if sex is not None:
                update_dict['sex'] = sex

            if birthday is not None:
                update_dict['birthday'] = birthday

            if user_op.update(id=id, **update_dict):
                self.finish(json.dumps({'state': 0, "message": "update success"}))
            else:
                self.finish(json.dumps({'state': 1, "message": "update into failed"}))

        except ParamExist as ex:
            LOG.error("Update error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))

        except Exception as ex:
            LOG.error("Update error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Update error'}))
