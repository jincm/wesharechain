#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
import logging
import json

LOG = logging.getLogger(__name__)


class UpdateStatusHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def post(self):
        try:
            id = self.get_argument('id', '')
            token = self.get_argument('token', '')
            status = self.get_argument('status', 0)
            #更新订单状态，先验证订单当前状态，只能往大了走，比如0-》1

            pass
        except ParamExist as ex:
            LOG.error("Update order status error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'Update order status params exit'}))
        except Exception as ex:
            LOG.error("Update order status error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Update order status error'}))