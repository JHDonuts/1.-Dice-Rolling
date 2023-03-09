# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



"""
----
Plot
----
"""
x = np.arange(0, 4*np.pi, 0.05)
ycos = np.cos(x)
ysin = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, ycos, 'b-', label="cos(x)")   #matplotlib default: blue solid line
ax.plot(x, ysin, 'r--', label="sin(x)" ) #red dashed line

ax.set_title("Trigonometric functions")
ax.set_xlabel("0 to 4pi")
ax.set_ylabel("cos(x) and sin(x)")
ax.legend()
plt.show()