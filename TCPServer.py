#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import traceback,sys
from time import strftime,localtime
from socketserver import ThreadingTCPServer,StreamRequestHandler
'''
TCPServer对象实例化参数有两个，一个是host,port的tuple，一个是handler类，把需要做的处理放到handler中。
ThreadingTCPServer自动做多线程处理。
自定义端口号，打印出已连接设备IP地址、端口号及连接时间。
打印出接收到的信息且回复发送成功信息。
Python3添加bytes类型，所以需要把发送信息通过encode()方法把str转化为bytes发送，接收时通过decode()方法把bytes转化为str才能打印。
'''
host = socket.gethostbyname(socket.gethostname())   #获取本机IP地址
port = int(input('请输入端口号：'))    #输入Server端口号

class myhandler(StreamRequestHandler):      #自定义handler类
    def handle(self):
        print(strftime('%Y-%m-%d %H:%M:%S', localtime()) + '   ' + str(self.client_address) + '    已连接!')     #打印出已连接的客户端地址
        while True:
            try:
                data = self.rfile.readline().strip().decode()       #使用rfile接收，无需考虑大小限制；
                                                                    # decode()函数把bytes类型转化为str
                #data = self.connection.recv(4096).decode()
                if data:                                            #若不加if else，则客户端断开连接后，仍然会继续打印空数据
                    print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'   '+str(self.client_address)+'    ' +data)
                    self.wfile.write('发送成功！'.encode())
                    #self.connection.send('发送成功！'.encode())
                else:
                    break
            except ConnectionResetError:
                print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'   '+str(self.client_address)+'    断开连接!')
                break
            except:
                traceback.print_exc()
try:
    server = ThreadingTCPServer((host,port),myhandler)
    server.serve_forever()
except OSError:
    print('端口被占用！')
    sys.exit()