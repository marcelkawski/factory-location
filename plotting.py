from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from environment import Environment

env1 = Environment()
env1.get_input()

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 20, 0.025)
Y = np.arange(0, 20, 0.025)
X, Y = np.meshgrid(X, Y)

dimension = len(X)

Z = np.zeros((dimension, dimension))
for x in range(dimension):
	for y in range(dimension):
		Z[x][y] = env1.all_cost((X[x][y], Y[x][y]))

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ax.set_zlim(775, 830)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.view_init(0, -90)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()