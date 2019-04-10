# coding:utf-8

from datetime import datetime, date
from datetime import timedelta
import re
import time
import struct
from urlparse import urlparse
from types import GeneratorType, NoneType
import collections
import six


TS_UNITS = ('year', 'month', 'day', 'hour', 'minute', 'sec')
_reg_val_code_pat = re.compile(r'^[\d]{8}$')
_num_pat = re.compile(r'^-?[a-f\d]+?$', re.I)
_email_pat = re.compile(r'^(?P<name>[a-zA-Z\d][_\.a-zA-Z\d]*)@(?P<domain>[a-zA-Z\d.]+\.[a-z]{2,4})$')
_uuid_pat = re.compile(r'^[a-f\d]{32}$')
_sha1_pat = re.compile(r'^[a-f\d]{40}$')
# 能用到203x年已经太牛叉了
_date_pat = re.compile(
    r'^(?P<year>[12]\d{3})-(?P<month>0[1-9]|1[012])-(?P<day>\d{1,2})(?:T(?P<hour>[01][0-9]|2[0-3]):(?P<minute>[0-5][0-9]):(?P<sec>[0-5][0-9]))?$')
_date_pat_s = re.compile(
    r'^(?P<year>[12]\d{3})-(?P<month>0[1-9]|1[012])-(?P<day>\d{1,2})(?:\s+(?P<hour>[01][0-9]|2[0-3]):(?P<minute>[0-5][0-9]):(?P<sec>[0-5][0-9]))?$')
_time_pat = re.compile(r'^(?P<hour>[01][0-9]|2[0-3]):(?P<minute>[0-5][0-9]):(?P<sec>[0-5][0-9])$')
_float_pat = re.compile(r'^-?\d+(\.\d+)?$')
_mac_pat = re.compile(r'^[a-f\d]{2}(?::[a-f\d]{2}){5}$', re.I)
_gsm_tid_pattern = re.compile(r'^[\d]{10,13}$', re.I)
_cdma_tid_pattern = re.compile(r'^[\da-f]{20}$', re.I)
_imei_pat = re.compile(r'^\d{15}$')
_imsi_pat = re.compile(r'^\d{15}$')
_ip_pat = re.compile(r'^(?:(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')
_port_pat = re.compile(r'^\d{2,5}$')
_ip_port_pat = re.compile(
    ''.join(('^', '(?P<ip>', _ip_pat.pattern[1:-1], '|[-_\da-z.]+):(?P<port>', _port_pat.pattern[1:-1], ')$')))
_cn_mobile_pat = re.compile(r'^\d{9,13}$')
_cn_mobile_cdma = re.compile(r'^(?:(?:(?:133|153|177|18[019])\d{1})|1700|173\d)\d{7}$') #电信
_user_name = re.compile(r'^[a-zA-Z][a-zA-Z\d\-_]{5,11}$') # 用户名
_password = re.compile(r'^(?![0-9]+$)(?![a-z]+$)(?![A-Z]+$)(?![,\.#%\'\+\*\-:;^_`]+$)[,\.#%\'\+\*\-:;^_`0-9A-Za-z]{8,20}$')
_merchant_name = re.compile(r'^[A-Za-z0-9\u4e00-\u9fa5]{3,50}$')


def is_reg_val_code(s):
    """
    帐号注册验证码
    """
    if not s or not isinstance(s, str):
        return False
    return _reg_val_code_pat.search(s)


def is_mobile(s):
    if not s or not isinstance(s, str):
        return False
    return _cn_mobile_pat.search(s)


def is_mobile_cdma(s):
    """
    电信手机号码
    :param s:
    :return:
    ^133\d{8}$
    ^153\d{8}$
    ^177\d{8}$
    ^18[0|1|9]\d{8}$
    ^1700\d{7}$
    """
    if not s or not isinstance(s,str):
        return False
    return _cn_mobile_cdma.search(s)



def is_gsm_tid(tid):
    """移动终端号码"""
    if not tid or not isinstance(tid, str):
        return False
    return _gsm_tid_pattern.search(tid)


def is_cdma_tid(tid):
    """电信终端号码"""
    if not tid or not isinstance(tid, str):
        return False
    return _cdma_tid_pattern.search(tid)


def is_time(v):
    if not v or not isinstance(v, str):
        return False
    return _time_pat.search(v)


def is_date(v):
    """
    20140424(T12:34:56)
    year, month, day, hour, minute, sec
    """
    if not v or not isinstance(v, str):
        return False
    m = _date_pat_s.search(v)
    if not m:
        return False

    month = int(m.groupdict().get('month'))
    day = int(m.groupdict().get('day'))
    if 2 == month and day > 29:
        return False
    return m

def is_password(v):
    """
    密码为8~20位数字,英文,符号至少两种组合的字符
    :param v:
    :return:
    """
    if not v or not isinstance(v, str):
        return False
    return _password.search(v)

def is_float(v):
    if not v or not isinstance(v, str):
        return False
    return _float_pat.search(v)


def is_num(v):
    if not v or not isinstance(v, str):
        return False
    return _num_pat.search(v)


def is_email(v):
    if not v or not isinstance(v, basestring):
        return False
    return _email_pat.search(v)

def is_user_name(v):
    if not v or not isinstance(v, basestring):
        return False
    return _user_name.search(v)


def is_uuidhex(v):
    if not v or not isinstance(v, str):
        return False
    return _uuid_pat.search(v)


def is_even(n):
    """
    偶数判定
    """
    return 0 == n % 2


def bs2unicode(bs):
    """
    basestring转换为python unicode类型
    """
    if not isinstance(bs, basestring):
        return bs
    if isinstance(bs, unicode):
        return bs
    return bs.decode('utf-8')


def bs2utf8(bs):
    if isinstance(bs, basestring):
        return bs.encode('utf-8') if isinstance(bs, unicode) else bs
    return bs


def to_list(x, default=None):
    if x is None:
        return default
    if not isinstance(x, collections.Iterable) or \
            isinstance(x, six.string_types):
        return [x]
    elif isinstance(x, list):
        return x
    else:
        return list(x)


