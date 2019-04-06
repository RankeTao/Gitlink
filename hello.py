# !/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver # 用来解决web服务器的http协议问题，它提供了不少属性方法，实现客户端和服务器端的互通
import tornado.ioloop     # 能够实现非阻塞socket循环，不能互通一次就结束呀。
import tornado.options    # 这是命令行解析模块
import tornado.web        # 必不可少的模块，它提供了一个简单的Web框架与异步功能，从而使其扩展到大量打开的连接，使其成为理想的长轮询。

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
# 通过tornado.options.define()定义了访问本服务器的端口，就是当在浏览器地址栏中输入http:localhost:8000的时候，才能访问本网站，
# 因为http协议默认的端口是80，为了区分，我在这里设置为8000,为什么要区分呢？因为我的计算机或许你的也是，已经部署了别的（或许是Nginx、Apache）
# 服务器了，它的端口是80,所以要区分开（也可能是故意不用80端口），并且，后面我们还会将tornado和Nginx联合起来工作，这样两个服务器在同一台计算机上，
# 就要分开喽
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting+", welcome you to read:www.baidu.com")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)]) 
    http_server = tornado.httpserver.HTTPServer(app) 
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()