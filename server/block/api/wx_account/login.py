#coding:utf-8

from tornado.web import RequestHandler
import tornado.httpclient
from six.moves.urllib import parse
from util.exception import ParamExist
from util import common_util
import logging
import json
from operation.wx_user import WxUserOp

from util.ini_client import ini_load

_conf = ini_load('config/service.ini')
game_dic_con = _conf.get_fields('game_wx')

LOG = logging.getLogger(__name__)

class LoginHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def post(self):
        try:
            code = self.get_argument('code', '')
            wx_name = self.get_argument('wx_name', '')
            invitation = self.get_argument('invitation', '')
            phone = self.get_argument('phone', '')
            verify_code = self.get_argument('verify_code', '')
            #判断下验证码



            #通过邀请码获取邀请人的用户id
            referrer_id = self.getReferrer(invitation)
            # 微信服务器验证
            url = "https://api.weixin.qq.com/sns/jscode2session"
            app_id = game_dic_con.get("appid")
            secret = game_dic_con.get("secret")
            params = {
                "appid": app_id,
                "secret": secret,
                "js_code": code,
                "grant_type": "authorization_code"
            }
            http_client = tornado.httpclient.HTTPClient()
            response = http_client.fetch("%s?%s" % (url, parse.urlencode(params)))
            dic_body = json.loads(response.body)
            openid = dic_body.get('openid')
            session_key = dic_body.get('session_key')
            # 存储openid和session_key,并返回识别session串
            op = WxUserOp()
            exit_app = op.info_by_openid(openid=openid)
            if exit_app:
                op.update(exit_app.get("id"), session_key=session_key)
                token = common_util.gen_token(exit_app.get("user_id"), 0)
                self.finish(json.dumps({'state': 0, 'id': exit_app.get("user_id"), 'token': token}))
            else:
                _ = op.create(code=code,
                              openid=openid,
                              session_key=session_key,
                              wx_name=wx_name,
                              referrer_id=referrer_id,
                              phone=phone,
                              )
                token = common_util.gen_token(_.get("user_id"), 0)
                self.finish(json.dumps({'state': 0, 'id': _.get("user_id"), 'token': token}))
        except ParamExist as ex:
            LOG.error("Wx login error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("Wx login error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'wx action error'}))

    def getReferrer(self, invitation):
        """
        通过邀请码获取邀请人的用户id
        :param invitation:
        :return:
        """
        return ""