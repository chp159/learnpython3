#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def triangles():
	b = [1]
	while True:
	    yield b
	    b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break