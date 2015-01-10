#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ma'
import torndb


class Model:
    table_name = None
    _where = dict()
    _order = None
    _limit_start = 0
    _limit_length = 0
    db = None

    def __init__(self):
        self.table_name = self.__class__.__name__
        self.db = torndb.Connection("", "")

    def query(self):
        pass

    def get(self):
        pass

    def get_field(self):
        pass

    def update(self, data):
        sql = "UPDATE table SET " + ",".join([k + "=" + str(v) for k, v in data.items()]) + self._build_sql()
        return self.db.update(sql)

    def insert(self, data):
        sql = "INSERT INTO " + self.table_name + "(" + ",".join(data.keys()) + ") VALUES (" + ",".join(
            data.values()) + ")"
        self.db.insert(sql)

    def delete(self):
        sql = "DELETE FROM " + self.table_name + self._build_sql()
        self.db.execute_rowcount(sql)

    def get_last_sql(self):
        pass

    def where(self, where):
        self._where.update(where)
        return self

    def order(self, column):
        self._order = column
        return self

    def limit(self, start, length=0):
        if length > 0:
            self._limit_start = start
            self._limit_length = length
        else:
            self._limit_start = 0
            self._limit_length = start
        return self

    def fetch_sql(self):
        return self._build_sql()

    def _build_sql(self):
        # 生成 WHERE
        where_str = ""
        for i in self._where:
            column = i.strip()
            contrast = "="
            if column.find(":") >= 0:  # 处理对比操作符=,>,<,>=等
                contrast = column[column.find(":") + 1:]
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
        where_str = where_str.lstrip(" AND ")  # 去除开始的AND操作，因为如果有操作符，会排到字典的后面。
        # 处理排序
        order_str = ",".join(self._order)
        # 拼装组合
        sql = ""
        if where_str:
            sql += "WHERE " + where_str
        if order_str:
            sql += " ORDER BY " + order_str
        if self._limit_length > 0:
            sql += " LIMIT " + self._limit_start + "," + self._limit_length
        return sql