# !/usr/bin/env python
# -*- coding：utf-8 -*-

import pymysql #python3.× 不支持MySQL

# 连接对象
conn = pymysql.Connect(host="localhost", user="root", password="123456", db="RankeTao_test", port=3306, charset="utf8") 
# pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.1' ([WinError 10061] 由于目标计算机积极拒绝，无法连接。
cur = conn.cursor()