#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#把n转换为字符串，正序字符串与倒序字符串相同，则为回数
def is_palindrome(n):
    return str(n)==str(n)[::-1]		#str(n)[::-1]的意思是把字符串str(n)从倒数第一个开始倒序排列
output = filter(is_palindrome, range(1, 1000))
print(list(output))