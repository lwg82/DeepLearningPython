# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:21:09 2019

@author: lwg
"""
import numpy as np
import matplotlib.pyplot as plt

# 偏导数定义
def gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp = x[idx]
        
        # f(x+h)
        x[idx] = tmp + h
        fxh1 = f(x)
        
        # f(x-h)
        x[idx] = tmp - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp   # 还原值
        
    return grad
        
    
def fun1(x):
    return x[0]*x[0] + x[1]*x[1];

print(gradient(fun1, np.array([3.0, 4.0]))) 

#plt.xlabel("x")
#plt.ylabel("y")

#plt.plot(x, y)

#plt.show()




