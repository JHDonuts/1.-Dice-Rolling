# -*- coding: utf-8 -*-


# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
------
Shapes
------
"""
fig, ax = plt.subplots()
ax.set_ylim([0, 20])
ax.set_xlim([-10, 10])
ax.axis('scaled')

# Rectangle
start_x = -2.5
start_y = 2
width = 5
height = 6
facecolor = 'gray'

rectangle = plt.Rectangle((start_x,start_y), width, height, 
                          fc=facecolor)
ax.add_patch(rectangle)

rectangle = plt.Rectangle((-0.5,2), 1, 2, fc="brown")
ax.add_patch(rectangle)

# Circle
start_x = -1
start_y = 6
radius = 0.5
facecolor = 'yellow'
edgecolor = 'black'
linewidth = 1

circle = plt.Circle((start_x,start_y), radius, 
                    fc=facecolor, ec=edgecolor, lw=linewidth)
ax.add_patch(circle)

circle = plt.Circle((1,6), 0.5, fc="yellow", ec="black", lw=1)
ax.add_patch(circle)

# Triangle
from matplotlib.patches import Polygon

start_xy = np.array([-2.5,8])
end_xy = np.array([2.5,8])
top_xy = np.array([0,10])

triangle = Polygon(np.vstack([start_xy, end_xy, top_xy]), color="red")
ax.add_patch(triangle)
plt.show()