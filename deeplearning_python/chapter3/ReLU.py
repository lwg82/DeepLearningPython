# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:46:09 2019

@author: lwg
"""

# http://www.numpy.org/
import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)



x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)

plt.plot(x, y)
plt.ylim(-1, 6) # y轴范围
plt.show()
