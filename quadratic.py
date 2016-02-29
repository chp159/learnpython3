#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
	d=b*b-4*a*c
	if d<0:
		return('无有理数解！')
	else:
		x1=(-b+math.sqrt(d))/(2*a) 
		x2=(-b-math.sqrt(d))/(2*a) 
	return x1,x2