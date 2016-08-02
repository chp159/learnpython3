#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time,sys
from time import strftime,localtime
'''
TCP客户端脚本，自定义服务器端IP及端口号，并选择是否自动发送，自定义发送时间间隔，自定义发送内容，自动保持心跳维护。
发送信息成功后接收服务端返回信息并打印。
Python3添加bytes类型，所以需要把发送信息通过encode()方法把str转化为bytes发送，接收时通过decode()方法把bytes转化为str才能打印。
'''

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_KEEPALIVE, 1)        #在客户端开启心跳维护

try:
    host = input('请输入服务端IP地址：')
    port = int(input('请输入服务端端口地址：'))
    client.connect((host, port))        #建立连接
except ConnectionRefusedError:
    print('服务端IP地址或端口错误，请检查！')
    sys.exit()

ias = input('是否自动发送（y/n）：')         #选择是否自动发送信息，y代表Yes，n代表No
if ias == 'y':
    t = float(input('请输入发送间隔（单位为秒，毫秒请输入小数，0为无间隔）：'))
    data = input('请输入要发送的信息：') + '\n'  # 输入需要发送的信息
    while True:
        client.sendall(data.encode())       #encode函数把str转化为bytes
        recvdata = client.recv(4096).decode()
        print(strftime('%Y-%m-%d %H:%M:%S', localtime()) + '  ' + recvdata)  # 打印出当前时间
        time.sleep(t) #如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点
else :
    while True:
        data = input('请输入要发送的信息：') + '\n'
        client.sendall(data.encode())  # encode函数把str转化为bytes
        recvdata = client.recv(4096).decode()
        print(strftime('%Y-%m-%d %H:%M:%S', localtime()) + '  ' + recvdata)  # 打印出当前时间