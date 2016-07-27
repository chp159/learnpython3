#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import traceback
from time import strftime,localtime
from socketserver import TCPServer,StreamRequestHandler

host = socket.gethostbyname(socket.gethostname())
port = int(input('请输入端口号：'))


class myhandler(StreamRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.rfile.readline().strip()
                print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'   '+str(self.client_address)+'    ' +data)
            except ConnectionResetError:
                #traceback.print_exc()
                print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'   '+str(self.client_address)+' disconnected!')
                break

server = TCPServer((host,port),myhandler)
server.serve_forever()