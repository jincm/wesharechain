#coding:utf-8

from tornado.web import StaticFileHandler
from settings import default_settings
from api import account, commodity, order
from api import verify_manage

def _handlers():
    return [
        (r'/gold/user$', account.UserHandler),
        (r'/user/login$', account.LoginHandler),

        (r'/gold/commodity$', commodity.CommodityHandler, default_settings),

        (r'/gold/order$', order.OrderHandelr),
        (r'/order/update_status$', order.UpdateStatusHandler),

        (r'/verify/code$', verify_manage.SendVerifyCodeHandler)
    ]

api_handlers = _handlers()