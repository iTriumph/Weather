#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web

from model.user_model import UserModel
from model.resource import ResourceModel


class BaseHandler(tornado.web.RequestHandler):
    user = None
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        email = self.get_argument("email", "")
        token = self.get_argument("token", "")
        user = UserModel.get_current_user(email, token)
        self.user = user
        return bool(self.user)


class HomeHandler(BaseHandler):
    def get(self):
        self.write("ok")


class SignUpHandler(BaseHandler):
    def post(self):
        email = self.get_argument("email", None)
        password = self.get_argument("password", None)
        result = UserModel.sign_up(email, password)
        self.write(result)


class SignInHandler(BaseHandler):
    def post(self):
        email = self.get_argument("email", None)
        password = self.get_argument("password", None)
        result = UserModel.sign_in(email, password)
        self.write(result)


class ResourceCreate(BaseHandler):
    """
    添加新资源
    """

    def post(self):
        url = self.get_argument("url", None)
        resource_type = self.get_argument("type", "text")
        r_model = ResourceModel(self.user.id)
        r_model.create(url,resource_type)
class ResourceList(BaseHandler):
    """
    获取资源列表
    """
    def post(self):
        r_model = ResourceModel(self.user.id)
        resource_list = r_model.recource_list()
