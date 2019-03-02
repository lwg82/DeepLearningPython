# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:20:10 2019

@author: lwg
"""

# http://www.numpy.org/
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1+np.exp(-x))



x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y轴范围
plt.show()
