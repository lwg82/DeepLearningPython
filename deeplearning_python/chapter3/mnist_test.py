# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:03:18 2019

@author: lwg
"""

import sys, os

sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_train.shape)