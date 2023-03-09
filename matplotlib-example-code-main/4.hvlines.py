# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
-----------------------------
Horizontal and Vertical Lines
-----------------------------
"""
fig, ax = plt.subplots(1,2)

ax[0].axhline(0.3, color='pink')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=10)
ax[0].axhline(0.6, linestyle=':', xmin=0.25, xmax=0.75, color='orchid')
ax[0].axhline(0.7, xmin=0.25, xmax=0.75, color=(0.1, 0.2, 0.5, 0.3))


ax[1].axvline(0.3, color='pink')
ax[1].axvline(0.4, linestyle='--', color='blue')
ax[1].axvline(0.5, color='cyan', linewidth=10)
ax[1].axvline(0.6, linestyle=':', ymin=0.25, ymax=0.75, color='orchid')
ax[1].axvline(0.7, ymin=0.25, ymax=0.75, color=(0.1, 0.2, 0.5, 0.3))

# Set x-axix and y-axis limits
ax[0].set_ylim([0.1, 0.9])
ax[1].set_xlim([0.1, 0.9])

# Set title to figure and subplots
fig.suptitle("Horizontal and vertical lines", fontsize=14)
ax[0].set_title('Horizontal lines', fontstyle='italic')
ax[1].set_title('Vertical lines',color='green',fontname='Arial')
plt.show()
