# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:21:09 2019

@author: lwg
"""
import numpy as np
import matplotlib.pyplot as plt

# 导数定义
def numerical_diff(f, x):
    h = 1e-4  # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

# 函数 y=0.01*x^2 + 0.1*x
def function_1(x):
    return 0.01*x**2 + 0.1*x

# 画直线
def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

    
    
x = np.arange(0.0, 20.0, 0.1) # 以0.1为单位
y = function_1(x)


tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, y)
plt.plot(x, y2)
plt.show()




