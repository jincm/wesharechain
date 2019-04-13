#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import or_, and_
from db import models
from db.base import *
from util import common_util


def model_query(model, session=None, order=False, read_deleted="no", desc=True, *args, **kwargs):
    """
    :param model:
    :param session: if present, the session to use
    """
    session = session or get_session()
    query = session.query(model, *args)

    if read_deleted == "no":
        query = query.filter_by(deleted=False)

    filter_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, tuple, set, frozenset)):
            column_attr = getattr(model, key)
            query = query.filter(column_attr.in_(value))
        else:
            filter_dict[key] = value

    if filter_dict:
        query = query.filter_by(**filter_dict)
    if order:
        if desc:
            query = query.order_by(model.create_time.desc())
        else:
            query = query.order_by(model.create_time)

    return query

def model_create(model, values):
    if not values.get('id'):
        values['id'] = common_util.create_id()
    ref = model()
    ref.update(values)
    session = get_session()
    with session.begin():
        ref.save(session)
        return values

def model_batch_create(model, lists):
    """
    批量创建
    :param lists: 带批量创建的数组
    :return:
    """
    session = get_session()
    with session.begin():
        try:
            for data in lists:
                if not data.get('id'):
                    data['id'] = common_util.create_id()  # str(uuid.uuid4())
                ref = model()
                ref.update(data)
                session.add(ref)
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex

def model_update(model, id, values):
    query = model_query(model).filter_by(id=id)
    result = query.update(values)
    if not result:
        return None
    return result

def model_get(model, id):
    query = model_query(model)
    result = query.filter_by(id=id).first()
    if not result:
        return None
    return result

def model_list(model, offset=0, limit=1000, **filters):
    query = model_query(model, order=True, **filters)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query.all()

def model_count(model, **filters):
    query = model_query(model, **filters)
    return query.count()

def model_deleted(model, id):
    session = get_session()
    with session.begin():
        query = model_query(model, session=session, id=id)
        query.update({
            "deleted": True
        },
        synchronize_session=False)


