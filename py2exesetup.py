#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe
import sys

'''
py2exe打包脚本
'''

sys.argv.append('py2exe')                           # 表示可以双击exe打开程序

py2exe_options = {
        "includes": ["sip"],                      # 需要包含的文件，sip为PyQt需要的文件
        "dll_excludes": ["MSVCP90.dll", ],       # 需要排除的dll文件，MSVCP90.dll文件如不排除，则可能报错
        "compressed": 1,                          # 压缩文件
        "optimize": 2,                            # 优化级别，默认为0
        "ascii": 0,                               # 不自动包含encodings和codecs
        "bundle_files": 1,                        # 值为1表示pyd和dll文件会被打包到单文件中，且不能从文件系统中加载python模块；
        # 值为2表示pyd和dll文件会被打包到单文件中，但是可以从文件系统中加载python模块
        }

setup(
      name='MyWindow',
      description='TCP服务端程序，配合TCPClient使用',
      version='1.0',
      console=[{'script': 'TCPClient.py', 'icon_resources': [(0, 'resource/1.ico')]}, ],     # 设置程序名称与exe的图标
      # console为命令行执行，改为windows则为程序窗口执行
      # icon_resources为图标目录
      zipfile=None,                           # 不生成zip文件
      options={'py2exe': py2exe_options}
      )
