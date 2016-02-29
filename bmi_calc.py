#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s1=input('请输入你的身高：')
s2=input('请输入你的体重：')
h=float(s1)
w=float(s2)
bmi=w/(h*h)
if bmi<=18.5:
	print('你的bmi指数是：%.1f,过轻'%bmi)
elif bmi<=25:
	print('你的bmi指数是：%.1f,正常'%bmi)
elif bmi<=28:
	print('你的bmi指数是：%.1f,过重'%bmi)
elif bmi<=32:
	print('你的bmi指数是：%.1f,肥胖'%bmi)
else:
	print('你的bmi指数是：%.1f,严重肥胖'%bmi)