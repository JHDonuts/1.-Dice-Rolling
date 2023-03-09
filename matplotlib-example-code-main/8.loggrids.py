# -*- coding: utf-8 -*-


# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
------------------
Log-axes and Text
------------------
"""
x = np.arange(0,10,0.01)
y = np.exp(x)

fig, ax = plt.subplots()

ax.plot(x,y)

ax.set_yscale('log')
ax.grid(which='both', linewidth=0.5, color=[.75, .75, .75, .5])
t = ax.text(8,y[1],'semi-log paper', fontweight='bold')
#plt.close("all") 
plt.show()
