#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time
from time import strftime,localtime

host = '192.168.31.127'
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
client.connect((host, port))        #建立连接
while True:
    client.sendall('Hello World!\n'.encode())       #encode函数把str转化为bytes
    print(strftime('%Y-%m-%d %H:%M:%S',localtime())+'  '+'Send data!')      #打印出当前时间
    time.sleep(1) #如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点
