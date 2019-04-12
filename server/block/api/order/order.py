
#coding:utf-8

from tornado.web import RequestHandler
from operation import order
import logging
import json
from util import common_util
from util.ini_client import ini_load

_conf = ini_load('config/service.ini')
_dic_con = _conf.get_fields('token')
timeout = _dic_con.get('timeout')

LOG = logging.getLogger(__name__)


class OrderHandelr(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        try:
            id = self.get_argument('id', '')
            order_type = self.get_argument('order_type', '')
            token = self.get_argument('token', '')
            status = self.get_argument('status', 0)
            limit = self.get_argument('limit', 0)
            offset = self.get_argument('offset', 0)
            is_timeout = common_util.validate_token_time(token, timeout)
            if is_timeout:
                self.finish({'state': 1,
                             'message': 'Token expired'
                             })
            op = order.OrderOp()
            order_list = op.lists(limit, offset, id, order_type, status)
            self.finish({
                'state': 0,
                'message': 'ok',
                'count': len(order_list),
                'data': order_list
            })
        except Exception as ex:
            LOG.error("Get order info error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Get order info error'}))

    def post(self):
        try:
            commodity_code = self.get_argument('commodity_code', '')
            order_type = self.get_argument('order_type', '')
            original_price = self.get_argument('original_price', '')
            real_price = self.get_argument('real_price', '')
            token = self.get_argument('token', '')
            is_timeout = common_util.validate_token_time(token, timeout)
            if is_timeout:
                self.finish({'state': 1,
                             'message': 'Token expired'
                             })

            op = order.OrderOp()
            op.create(commodity_code, order_type, original_price, real_price)
            self.finish({
                'state': 0,
                'message': 'ok',
            })
        except Exception as ex:
            LOG.error("Get order info error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Get order info error'}))