#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import re

__author__ = 'Ma'


class UserModel:
    def __init__(self):
        pass

    @staticmethod
    def sign_in():
        """
        处理登录的问题
        """
        return None

    @staticmethod
    def sign_up(email, password):
        return UserModel()

    @staticmethod
    def password():
        """
        修改密码，找回密码
        :return:
        """
        pass

    @staticmethod
    def check_email(email):
        """
        检查Email格式
        """
        if re.match("/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/", email) is not None:
            return True
        else:
            return False

    @staticmethod
    def md5(string):
        """
        MD5一个字符串
        """
        h = hashlib.md5()
        h.update(string)
        return h.hexdigest()