from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# 定义基始初量
a = 0.529
A3 = 1
B = 1

# 定义输出图像函数
def outputimg(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)



X = np.arange(0, np.pi)

Y = np.arange(0, np.pi*2)
R = 8
X, Y = np.meshgrid(X, Y)
Z = A3*R*(np.exp(-B*R/2))*np.sqrt(3/(4*np.pi))*np.sin(X)*np.cos(Y)
outputimg(X, Y, Z)

plt.show()