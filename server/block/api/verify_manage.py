#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
import logging
import json

LOG = logging.getLogger(__name__)


class SendVerifyCodeHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def post(self):
        try:
            pass
        except ParamExist as ex:
            LOG.error("order create error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'order create error'}))