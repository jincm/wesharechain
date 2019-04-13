# coding=utf-8

import uuid
import time
from util import crypto_rc4
from random import randint

def create_id():
    return uuid.uuid4().get_hex()

def create_verifycode():
    """
    生成注册验证码
    :return:
    """
    return "888888"
    verify_code = ''.join((str(randint(0, 9)) for _ in range(6)))
    return verify_code

def gen_token(sign, time):
    """
    根据签名生成token
    :param sign: 签名内容
    :param time: 签名有效时长
    :return:
    """
    content = ":".join((sign, str(time)))
    token = crypto_rc4.encrypt(content, crypto_rc4.SECRET_KEY)
    return token

def dgen_token(token):
    """
    解析token
    :param token:
    :return:
    """
    _ = crypto_rc4.decrypt(token, crypto_rc4.SECRET_KEY)
    _ = _.split(":")
    if(len(_)!=2):
        return "", -1
    sign, time = _.split(":")
    return sign, int(time)


def send_vrifycode(verify_code):
    pass