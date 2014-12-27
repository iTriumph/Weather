#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ma'


class Model:
    table_name = None

    def __init__(self):
        self.table_name = self.__class__.__name__

    def query(self):
        pass

    def get(self):
        pass

    def get_field(self):
        pass

    def update(self, data, where):
        pass

    def insert(self, data):
        pass

    def delete(self, where):
        pass

    def get_last_sql(self):
        pass

    def where(self):
        pass

    def order(self):
        pass

    def limit(self):
        pass

    def fetch_sql(self):
        pass
