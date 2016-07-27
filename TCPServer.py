#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import traceback
from time import strftime,localtime
from socketserver import TCPServer,StreamRequestHandler
'''
TCPServer对象实例化参数有两个，一个是host,port的tuple，一个是handler类，把需要做的处理放到handler中。
'''
host = socket.gethostbyname(socket.gethostname())   #获取本机IP地址
port = int(input('请输入端口号：'))    #输入Server端口号
#BUF_SIZE = 4096

class myhandler(StreamRequestHandler):      #自定义handler类
    def handle(self):
        while True:
            try:
                data = self.rfile.readline().strip().decode()       #使用rfile接收，无需考虑大小限制；
                                                                    # decode()函数把bytes类型转化为str
                #data = self.connection.recv(BUF_SIZE)
                print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'   '+str(self.client_address)+'    ' +data)
            except ConnectionResetError:
                #traceback.print_exc()
                print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'   '+str(self.client_address)+'    disconnected!')
                break

server = TCPServer((host,port),myhandler)
server.serve_forever()