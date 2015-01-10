#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torndb

db = torndb.Connection(host="127.0.0.1:3306", database="test", user="root", password="123456")