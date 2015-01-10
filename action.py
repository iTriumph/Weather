#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web

from model.user_model import UserModel
from model.resource import ResourceModel


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass


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
        self.write("")