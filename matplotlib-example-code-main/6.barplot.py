# -*- coding: utf-8 -*-


# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
--------
Bar Plot
--------
"""
# Data
people = ["Student A", "Student B"]
studentA = np.array([90,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange(len(studentA))

# Figure
fig, ax = plt.subplots(1,2)

# Plots
ax[0].bar(x, studentA, width=0.3)
ax[1].bar(x, studentB, width=0.3)

# Aesthetics
for i in range(len(ax)):
    ax[i].set_ylim([0, 100])
    ax[i].set_title(people[i])
    ax[i].set_xlabel("exercises")
    ax[i].set_ylabel("mark (%)")
    ax[i].set_xticks([0,1,2,3])
    ax[i].set_xticklabels(["ex1","ex2","ex3","ex4"])

# Extra: fixes the subplots separation
fig.tight_layout()
plt.show()



"""
------------------
Bar Plot (grouped)
------------------
"""
fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/2, studentA, width, label='Student A')
s2bars = ax.bar(x + width/2, studentB, width, label='Student B')
