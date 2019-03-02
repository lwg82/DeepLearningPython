# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:58:41 2019

@author: lwg
激活函数
"""

import numpy as np
import matplotlib.pylab as plt

"""
主要用于 隐藏层
"""    

# 阶跃激活函数
def step_function(x):
    return np.array(x>0, dtype=np.int)

# sigmoid 激活函数
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

# Relu 激活函数
def relu_function(x):
    return np.maximum(0, x)  # maximum 逐位比较取其大者

#############################################
"""
主要用于 输出层
"""    

# 恒等 激活函数
def identity_function(x):
    return x

# softmax 激活函数
def softmax_function(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

    

#############################################
# 测试阶跃函数
def test_step_function():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) #指定 y 轴范围
    plt.show()
    
 # 测试 sigmoid 函数
def test_sigmoid():
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid_function(x)
    
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
    
def test_softmax():
    a = np.array([0.3, 2.9, 4.0])
    y = softmax_function(a)
    print(y)
    print(np.sum(y))
    
def test():
    test_step_function()
    test_sigmoid()
    test_softmax()

if __name__ == '__main__':
    test()