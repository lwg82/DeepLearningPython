# http://www.numpy.org/
import numpy as np
import matplotlib.pyplot as plt


# 阶跃函数 1
def StepFunction1(x):
    if x>0:
        return 1
    else:
        return 0

# 阶跃函数 2
def StepFunction2(x):
    y = x>0
    return y.astype(np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = StepFunction2(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y轴范围
plt.show()
