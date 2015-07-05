#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import torndb

db = torndb.Connection(host="127.0.0.1:3306", database="test", user="root", password="123456")


class ResourceModel:
    """
    个人资源管理
    """
    user_id = 0
    types = ("text", "pdf", "image")

    def __init__(self, user_id):
        self.user_id = int(user_id)

    def create(self, url, resource_type="text"):
        """
        添加资源
        """

        resource_type = resource_type if self.types.index(resource_type) else "text"

        resource_info = db.get("SELECT `id` FROM `resource` WHERE `url` = %s ", url)
        if resource_info:
            resource_id = resource_info.id
        else:
            resource_id = db.insert("INSERT INTO `resource` (`url`,`resource_type`,`create_date`) VALUES (%s,%s,%s)",
                                    url, resource_type, time.time())

        result = db.insert(
            "INSERT INTO `user_resource` (`user_id`,`resource_id`,`resource_type`,`url`,`create_date`) VALUES \
            (%s,%s,%s,%s,%s)", self.user_id, resource_id, resource_type, url, time.time())
        return result

    def resource_list(self, resource_type="all", start=0, length=50):
        """
        获取资源的列表
        """
        resource_type = resource_type if self.types.index(resource_type) else "all"
        if resource_type == "all":
            resource_list = db.query(
                "SELECT * FROM user_resource WHERE `user_id`=%s ORDER BY create_date ASC LIMIT %s,%s",
                self.user_id, resource_type, start, length)
        else:
            resource_list = db.query(
                "SELECT * FROM user_resource WHERE user_id=%s AND resource_type=%s \
                ORDER BY create_date ASC LIMIT %s,%s", self.user_id, resource_type, start, length)
        return resource_list

    def delete(self, resource_id):
        result = db.update("DELETE FROM user_resource WHERE user_id = %s AND resource_id = %s", self.user_id,
                           resource_id)
        return result

print ResourceModel(1).resource_list("text")