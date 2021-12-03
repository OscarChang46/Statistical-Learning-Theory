import numpy as np
import matplotlib.pyplot as plt

mean = [0,0,0]
cov = [[10, 50, 0],
       [50, 10, 0],
       [0, 0, 10]]

out= np.random.multivariate_normal(mean, cov, 50000)
x,y,z = out[:,0],out[:,1],out[:,2]

Z = Z = np.sin(np.pi*x)*np.sin(np.pi*y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x,y,z, alpha = 0.05, s = 1)
#ax.contour(x, y, Z, 10, lw=3, colors="k", linestyles="solid")
plt.show()