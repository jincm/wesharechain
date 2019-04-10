#coding:utf-8

from tornado.web import RequestHandler
from util.exception import ParamExist
import logging
import json
import os
import time
from PIL import Image

LOG = logging.getLogger(__name__)


class CommodityHandler(RequestHandler):
    def initialize(self, static_path, commodity_path, **kwds):
        self.static_path = static_path
        self.commodity_path = commodity_path

    def get(self):
        pass

    def post(self):
        try:
            #获取商品图片
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


        except ParamExist as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("commodity  create error:%s" % ex)
            self.finish(json.dumps({'state': 10, 'message': 'commodity  create error'}))

    def put(self):
        pass

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