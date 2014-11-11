__author__ = 'Kheder'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import griddata
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import sys

def xyz_ret(file):
    f = open(file, 'r')

    xyz = []
    for i in f:
        ret = i.replace('\n','')
        xyz.append(map(float,(ret.split('\t'))))

    xyz =  np.array(xyz)
    return xyz[:,0],xyz[:,1],xyz[:,2]


x,y,z = xyz_ret('roboter.py')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))

X, Y = np.meshgrid(xi, yi)
Z = griddata(x, y, z, xi, yi)

surf = ax.plot_surface(X, Y, Z, rstride=6, cstride=6, cmap=cm.jet,
        linewidth=0)

ax.set_zlim3d(min(z), max(z))

ax.w_zaxis.set_major_locator(LinearLocator(10))
ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()