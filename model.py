#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ma'


class Model:
    table_name = None
    _where = None
    _order = None
    _limit = None

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

    def where(self, where):
        self._where = where
        return self

    def order(self, column):
        self._order = column
        return self

    def limit(self, limit):
        self._limit = limit
        return self

    def fetch_sql(self):
        self._build_sql()

    def _build_sql(self):
        #  生成 WHERE
        where_str = ""
        for i in self._where:
            column = i.strip()
            contrast = "="
            if column.find(":") >= 0:  # 处理对比操作符=,>,<,>=等
                contrast = column[column.find(":")+1:]
                column = column[0:column.find(":")]

            if column.startswith("&"):  # 处理 AND
                column = column[1:]
                where_str += " AND " + column
            elif column.startswith("|"):  # 处理 OR
                column = column[1:]
                where_str += " OR " + column
            else:  # 默认 AND
                if len(self._where) > 1:
                    where_str += " AND " + column
                else:
                    where_str += column

            where_str += contrast + str(self._where.get(i))

        order_str = ",".join(self._order)
        print order_str



model = Model()
print model.where({"name": "ma", "|age:>": 22}).order(['name','age']).fetch_sql()
print model._where
