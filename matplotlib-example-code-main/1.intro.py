# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
---------------------------
Matplotlib Object Hierarchy
---------------------------
"""

# Basic figure
y = np.linspace(-1, 1, 5)
x = np.arange(5)

fig = plt.figure()    #create a figure object
ax = fig.subplots()   #create an axes object in the figure (position, grid rows, grid columns)
line1 = ax.plot(x,y)  #create a line

# Add another line
y2 = np.linspace(-2, 2, 5)
line2 = ax.plot(x,y2)

# Figure with different subplots
number_rows = 3
number_columns = 2
fig2 = plt.figure()
ax2 = fig2.subplots(number_rows,number_columns)
ax2[2,1].plot(x,y)
plt.show()
# Handy commands
#plt.gcf()
#plt.gca()
#plt.clf()
#plt.cla()
#plt.close(fig) 
#plt.close("all") 

