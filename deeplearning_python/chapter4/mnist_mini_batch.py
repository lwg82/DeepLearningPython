# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:39:34 2019

@author: lwg
"""


import sys, os
import numpy as np

sys.path.append(os.pardir)
from dataset.mnist import load_mnist


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
normalize=True, one_hot_label=True)


print(x_train.shape[0])

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size) # 选出一批数据，得到数据的索引
print(batch_mask)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]