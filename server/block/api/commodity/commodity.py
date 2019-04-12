#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
import logging
import json
import os
import time
from PIL import Image
from util import common_util
from operation import commodity
from util.ini_client import ini_load

_conf = ini_load('config/service.ini')
_dic_con = _conf.get_fields('token')
timeout = _dic_con.get('timeout')

LOG = logging.getLogger(__name__)


class CommodityHandler(RequestHandler):
    def initialize(self, static_path, commodity_path, **kwds):
        self.static_path = static_path
        self.commodity_path = commodity_path

    def get(self):
        try:
            id = self.get_argument('id', '')
            name = self.get_argument('name', '')
            token = self.get_argument('token', '')
            limit = self.get_argument('limit', 0)
            offset = self.get_argument('offset', 0)
            is_timeout = common_util.validate_token_time(token)
            if is_timeout:
                self.finish({'state': 1,
                             'message': 'Token expired'
                             })
            op = commodity.CommodityOp()
            commodity_list = op.lists(limit, offset, id, name)
            self.finish({
                'state': 0,
                'message': 'ok',
                'count': len(commodity_list),
                'data': commodity_list
            })
        except Exception as ex:
            LOG.error("Get order info error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'Get order info error'}))

    def post(self):
        try:
            name = self.get_argument('name', '')
            describe = self.get_argument('describe', '')
            original_price = self.get_argument('original_price', '')
            real_price = self.get_argument('real_price', '')
            commodity_type = self.get_argument('commodity_type', '')
            token = self.get_argument('token', '')
            # 获取商品图片
            imgs = self.request.files.get('image', '')
            if not imgs:
                LOG.error("image is none")
                self.finish(json.dumps({'state': 3, 'message': 'image is none'}))
                return
            img = imgs[0]
            filename = img['filename']
            filename = str(int(time.time())) + "." + filename.rpartition(".")[-1]
            file_path = self.static_path + self.commodity_path + filename
            with open(file_path, 'wb') as up:
                up.write(img['body'])

            self._img_resize(file_path)

            is_timeout = common_util.validate_token_time(token, timeout)
            if is_timeout:
                self.finish({'state': 1,
                             'message': 'Token expired'
                             })
            op = commodity.CommodityOp()
            op.create(name, describe, original_price, real_price, commodity_type, file_path)
            self.finish({
                'state': 0,
                'message': 'ok',
            })

        except ParamExist as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'commodity  create error'}))

    def put(self):
        try:
            id = self.get_argument('id', '')
            name = self.get_argument('name', '')
            describe = self.get_argument('describe', '')
            original_price = self.get_argument('original_price', '')
            real_price = self.get_argument('real_price', '')
            commodity_type = self.get_argument('commodity_type', '')
            token = self.get_argument('token', '')
            # 获取商品图片
            imgs = self.request.files.get('image', '')
            if not imgs:
                LOG.error("image is none")
                self.finish(json.dumps({'state': 3, 'message': 'image is none'}))
                return
            img = imgs[0]
            filename = img['filename']
            filename = str(int(time.time())) + "." + filename.rpartition(".")[-1]
            file_path = self.static_path + self.commodity_path + filename
            with open(file_path, 'wb') as up:
                up.write(img['body'])

            self._img_resize(file_path)

            is_timeout = common_util.validate_token_time(token, timeout)
            if is_timeout:
                self.finish({'state': 1,
                             'message': 'Token expired'
                             })
            op = commodity.CommodityOp()
            op.update(id, name, describe, original_price, real_price, commodity_type, file_path)
            self.finish({
                'state': 0,
                'message': 'ok',
            })

        except ParamExist as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'commodity  create error'}))

    def _img_resize(self, path):
        """
        对大于2M的图片进行缩放
        :param path:
        :return:
        """
        fsize = os.path.getsize(path)
        if fsize <= 2097152:
            return
        ims = Image.open(path)
        s = 1920
        w = ims.width / s
        h = ims.height / s
        if w > h:
            width = s
            height = int(s * (h / w))
        else:
            height = s
            width = int(s * (w / h))

        ims = ims.resize((width, height))
        ims.save(path)