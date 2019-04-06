# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the url structure of website
"""

import sys # uft-8 兼容汉字
# sys.getdefaultencoding() 默认编码utf-8
from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
]