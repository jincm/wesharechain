#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base as BaseDB

class Base(object):
    def __init__(self):
        self.exampledb = BaseDB()

    def create(self,  **kwargs):
        return self.exampledb.create(**kwargs)

    def batch_create(self, lists, **kwargs):
        self.exampledb.batch_create(lists)

    def update(self, id="", **kwargs):
        return self.exampledb.update(id, **kwargs)

    def info(self, id=""):
        return self.exampledb.info(id)

    def lists(self, offset=0, limit=1000, **kwargs):
        return self.exampledb.lists(offset, limit, **kwargs)

    def delete(self, id=""):
        self.exampledb.delete(id)

    def views(self, models):
        if not models:
            return []
        if isinstance(models, dict):
            return models
        if isinstance(models, list):
            result = []
            for model in models:
                result.append(model if isinstance(model, dict) else model.to_dict())
            return result
        return models.to_dict()