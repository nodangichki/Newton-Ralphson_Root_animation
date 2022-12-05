#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from sympy import *
"""
Created on Tue Dec  6 01:12:20 2022

@author: nodan
"""
t = Symbol('t')
required_eval_time = 27
t1 = 0
t2 = 0
x = [0,10,15,20,22.5,30]
y = [0,227.04,362.78,517.35,602.97,901.67]
v_of_t = 0
plt.plot(x,y,marker='o',linestyle='')
for i in range (0,len(x)):
    if(x[i] > required_eval_time):
        t1 = x[i-1]
        time1 = i-1
        t2 = x[i]
        time2 = i
        break

v_of_t = y[time1]+((y[time2]-y[time1])/(t2-t1))*(t-t1)

print(f' At time {required_eval_time} velocity is {round(v_of_t.subs(t,16),3)}')