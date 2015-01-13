#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import random
import re
import string
import time
import torndb

db = torndb.Connection(host="127.0.0.1:3306", database="test", user="root", password="123456")


class UserModel:
    def __init__(self):
        pass

    @staticmethod
    def get_current_user(email, token):
        """
        认证登录用户
        """
        if UserModel.check_email(email) is False or len(token) < 32:
            return False
        info = db.get("SELECT * FROM `user` WHERE `email` = %s AND `token` = %s LIMIT 1", email,
                      token)
        return info

    @staticmethod
    def sign_in(email, password):
        """
        处理登录的问题
        -1密码错误
        -2尚未注册
        -3邮箱或者密码格式错误
        """
        if UserModel.check_email(email) is False or len(password) < 6:
            return -3
        info = db.get("SELECT * FROM `user` WHERE `email` = %s AND `password` = %s LIMIT 1", email,
                      UserModel.md5(email + password))
        if info:
            return info
        else:
            is_reg = db.get("SELECT `id` FROM `user` WHERE `email` = %s LIMIT 1", email)
            if is_reg:
                return -2
            else:
                return -1

    @staticmethod
    def sign_up(email, password):
        """
        注册功能
        """
        if UserModel.check_email(email) is False or len(password) < 6:
            return False

        is_reg = db.get("SELECT `id` FROM `user` WHERE `email` = %s LIMIT 1", email)
        if is_reg:
            return False

        user_id = db.insert("INSERT INTO `user` (`email`,`password`,`token`,`regtime`) VALUES (%s,%s,%s,%s)", email,
                            UserModel.md5(email + password), UserModel.md5(email + UserModel.get_random_str()),
                            int(time.time()))
        return user_id

    @staticmethod
    def reset_password(email, old_password, new_password):
        """
        修改密码
        """
        info = db.get("SELECT * FROM user WHERE `email` = %s AND `password` = %s LIMIT 1", email,
                      UserModel.md5(email + old_password))
        if info or len(new_password) < 6:
            result = db.update("UPDATE user SET password = %s,token=%s WHERE email=%s AND password=%s LIMIT 1",
                               UserModel.md5(email + new_password), UserModel.md5(email + UserModel.get_random_str()),
                               email, UserModel.md5(email + old_password))
            return bool(result)
        else:
            return False

    @staticmethod
    def forget_password():
        """
        忘记密码
        """
        pass

    @staticmethod
    def check_email(email):
        """
        检查Email格式
        """
        if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email) is not None:
            return True
        else:
            return False

    @staticmethod
    def md5(md5_string):
        """
        MD5一个字符串
        """
        h = hashlib.md5()
        h.update(md5_string)
        return h.hexdigest()

    @staticmethod
    def get_random_str(length=10):
        return ''.join(random.sample(string.ascii_lowercase + string.digits, length))