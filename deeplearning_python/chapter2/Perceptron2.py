import numpy as np


# 与门函数实现
def AND(x1, x2):
    x = np.array([x1, x2]) # 输入
    w = np.array([0.5, 0.5]) # 权重
    b = -0.7   # 偏置
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 与非门
def NAND(x1, x2):
    x = np.array([x1, x2]) # 输入
    w = np.array([-0.5, -0.5]) # 权重
    b = 0.7   # 偏置
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 或门
def OR(x1, x2):
    x = np.array([x1, x2]) # 输入
    w = np.array([0.5, 0.5]) # 权重
    b = -0.2   # 偏置
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 异或门
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(AND(0, 0)) # 0
print(AND(1, 0)) # 0
print(AND(0, 1)) # 0
print(AND(1, 1)) # 1

print(NAND(0, 0)) # 1
print(NAND(1, 0)) # 1
print(NAND(0, 1)) # 1
print(NAND(1, 1)) # 0

print(OR(0, 0)) # 0
print(OR(1, 0)) # 1
print(OR(0, 1)) # 1
print(OR(1, 1)) # 1

print(XOR(0, 0)) # 0
print(XOR(1, 0)) # 1
print(XOR(0, 1)) # 1
print(XOR(1, 1)) # 0