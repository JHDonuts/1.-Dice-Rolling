# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
------------------------
Basic Plotting Functions
------------------------
"""
y1 = np.arange(0,110,10)
y2 = np.random.random(11)
x = np.arange(11)

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x,y1) 
ax[0,1].scatter(x,y2)
ax[1,0].bar(x,y1)
ax[1,1].barh(x,y1)
plt.show()