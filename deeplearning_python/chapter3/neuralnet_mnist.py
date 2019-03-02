# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:51:57 2019

@author: lwg
"""
import numpy as np
import pickle
import sys, os
sys.path.append(os.pardir)


from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


# 得到测试数据
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

# 读取学习好的权重和偏置
def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y
    
        
network = init_network()
x, t = get_data()



#print(x.shape)
#print(np.ndim(x)) # 维度

#print(x[0])
#print(x[0].shape) # 28 * 28

W1 = network['W1']
print(W1.shape)

W2 = network['W2']
print(W2.shape)

W3 = network['W3']
print(W3.shape)

# 识别精度
accuracy_cnt = 0
# 单张图片分类
#for i in range(len(x)):
#    y = predict(network, x[i])
#    p = np.argmax(y) # 概率最高的元素索引
#    if p==t[i]:
#        accuracy_cnt += 1
        
#print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

#多张图片分类，批分类
batch_size=100

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p==t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))