#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Table, MetaData, UniqueConstraint, ForeignKey

from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from base import get_engine, ModelBase

Base = declarative_base()

def _to_dict(model_obj):
    result = {}
    for c in model_obj.__table__.columns:
        if isinstance(getattr(model_obj, c.name, None), datetime):
            if c.name == "birthday":
                result.update({c.name: getattr(model_obj, c.name, None).strftime('%Y-%m-%d')})
            else:
                result.update({c.name: getattr(model_obj, c.name, None).strftime('%Y-%m-%d %H:%M:%S')})
        elif isinstance(getattr(model_obj, c.name, None), Base):
            result.update({c.name: getattr(model_obj, c.name, None).to_dict()})
        else:
            result.update({c.name: getattr(model_obj, c.name, None)})
    return result


class UserInfo(Base, ModelBase):
    __tablename__ = 'user_info'
    id = Column(VARCHAR(36), primary_key=True)
    name = Column(VARCHAR(100))
    nick_name = Column(VARCHAR(100))
    pwd = Column(VARCHAR(50))
    phone = Column(VARCHAR(36))
    activate = Column(Integer, default=0)
    sex = Column(Integer, default=0)
    birthday = Column(DateTime)
    invitation = Column(VARCHAR(10))
    referrer_id = Column(VARCHAR(36))
    gold_account = Column(VARCHAR(50))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class WxUserinfo(Base, ModelBase):
    __tablename__ = 'wx_userinfo'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36), nullable=False)
    openid = Column(VARCHAR(50) , nullable=False)
    code = Column(VARCHAR(36), nullable=False)
    session_key = Column(VARCHAR(50), nullable=False)
    wx_name = Column(VARCHAR(50))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class VerifyManage(Base, ModelBase):
    __tablename__ = 'verify_manage'
    id = Column(VARCHAR(36), primary_key=True)
    phone = Column(VARCHAR(36))
    email = Column(VARCHAR(50))
    verify_code = Column(VARCHAR(36))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class GoldOrder(Base, ModelBase):
    __tablename__ = 'gold_order'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36), nullable=False)
    commodity_code = Column(VARCHAR(36), nullable=False)
    order_type = Column(Integer, default=0)
    original_price = Column(Float, default=0)
    real_price = Column(Float, default=0)
    status = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class GoldCommodity(Base, ModelBase):
    __tablename__ = 'gold_commodity'
    id = Column(VARCHAR(36), primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    describe = Column(VARCHAR(500))
    original_price = Column(Float, default=0)
    real_price = Column(Float, default=0)
    commodity_type = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

def register_db():
    engine = get_engine()
    Base.metadata.create_all(engine)


def unregister_db():
    engine = get_engine()
    Base.metadata.drop_all(engine)