#!/usr/bin/python
# -*- coding: utf-8 -*-
from db import api

class Base(object):
    def __init__(self):
        self.model=None

    def create(self, **kwargs):
        if self.model==None:
            return
        return api.model_create(self.model, kwargs)

    def batch_create(self, lists):
        if self.model==None:
            return
        api.model_batch_create(self.model, lists)

    def update(self, id="", **kwargs):
        if self.model==None:
            return
        return api.model_update(self.model, id, kwargs)

    def info(self, id=""):
        if self.model==None:
            return
        return api.model_get(self.model, id)

    def lists(self, offset=0, limit=1000, **kwargs):
        if self.model==None:
            return
        return api.model_list(self.model, offset, limit, **kwargs)

    def counts(self, **kwargs):
        if self.model==None:
            return
        return api.model_count(self.model, **kwargs)

    def delete(self, id=""):
        if self.model==None:
            return
        api.model_deleted(self.model, id)