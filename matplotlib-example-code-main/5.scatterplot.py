# -*- coding: utf-8 -*-


# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
------------
Scatter Plot
------------
"""
x = np.array([2,4,6,7,4,2,5,7,8,9,4,2,1])
y = np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])

fig, ax = plt.subplots(1,3)
ax[0].scatter(x,y)
ax[0].set_title('default')

ax[1].scatter(x, y, 50, marker='+')
ax[1].set_title('size = 50, style = +')

crosses = ax[2].scatter(x, y, 200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, 50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

#3D
z = np.array([0,1,4,3,5,1,2,5,7,5,9,8,5])
fig = plt.figure()
ax = np.array([fig.add_subplot(1, 3, 1, projection='3d'),
               fig.add_subplot(1, 3, 2, projection='3d'),
               fig.add_subplot(1, 3, 3, projection='3d')])

ax[0].scatter(x,y,z)
ax[0].set_title('default')

ax[1].scatter(x, y, z, s=50, marker='+')
ax[1].set_title('size = 50, style = +')

crosses = ax[2].scatter(x, y, z, s=200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, z, s=50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')
plt.show()