
#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
import logging
import json

LOG = logging.getLogger(__name__)

class OrderHandelr(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        try:
            pass
        except Exception as ex:
            LOG.error("Get order info error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Get order info error'}))

    def post(self, *args, **kwargs):
        pass