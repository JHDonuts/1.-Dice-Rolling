# -*- coding: utf-8 -*-


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

# Handy commands
#plt.gcf()
#plt.gca()
#plt.clf()
#plt.cla()
#plt.close(fig) 
#plt.close("all") 



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



"""
-----------------------------
Horizontal and Vertical Lines
-----------------------------
"""
fig, ax = plt.subplots(1,2)

ax[0].axhline(0.3, color='red')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=10)
ax[0].axhline(0.6, linestyle=':', xmin=0.25, xmax=0.75, color='orchid')
ax[0].axhline(0.7, xmin=0.25, xmax=0.75, color=(0.1, 0.2, 0.5, 0.3))


ax[1].axvline(0.3, color='red')
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



"""
------------------
Bar Plot (grouped)
------------------
"""
fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/2, studentA, width, label='Student A')
s2bars = ax.bar(x + width/2, studentB, width, label='Student B')



"""
------
Task 1
------
"""
ax.set_ylim([0, 100])
ax.set_title(people[i])
ax.set_xlabel("exercises")
ax.set_ylabel("mark (%)")
ax.set_xticks([0,1,2,3])
ax.set_xticklabels(["ex1","ex2","ex3","ex4"])
ax.legend()

for i in range(len(studentA)):
    s1bars[i].set_linewidth(3.5)
    s2bars[i].set_linewidth(3.5)
    if studentA[i] < 50:
        s1bars[i].set_edgecolor('red') 
        s2bars[i].set_edgecolor('red')



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
plt.close("all") 



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



"""
---------------
Save and Export
---------------
"""
# Ask what formats matplotlib supports:
formats = plt.gcf().canvas.get_supported_filetypes()

fig.savefig("house.jpg")



"""
----------------------------
Data Analytics Visualisation
----------------------------
"""
# Get the Iris dataset
dataRaw = np.loadtxt("iris-head-num.txt", delimiter=',', dtype='object')
# Get the header (first row)
header = dataRaw[0,:]
# Get the data (second row till end; 1-4th columns). Convert them to float
data = dataRaw[1:,:4]
data = np.vstack(data.astype(np.float32))
# Get the labels (second row; 4th columns)
labels = np.vstack(dataRaw[1:,4].astype(np.int32))
# Find unique labels and frequency
labelsUn, labelsCounts = np.unique(labels, return_counts=True)

# Find average, maximum, minimum and stand deviation of each column per category
nrows,ncols = np.shape(data) #number of rows and columns
nclasses = len(labelsUn)     #number of unique categories
#Initialise an nclasses-by-ncols per statistic
average = np.zeros((nclasses,ncols)) #mean
maxi = np.zeros((nclasses,ncols))    #maximum
mini = np.zeros((nclasses,ncols))    #minimum
sd = np.zeros((nclasses,ncols))      #standard deviation
for i in labelsUn:
    indexes = np.reshape(labels==i,nrows)
    average[i-1,:] = np.mean(data[indexes,:],axis=0)
    maxi[i-1,:] = np.max(data[indexes,:],axis=0)
    mini[i-1,:] = np.min(data[indexes,:],axis=0)
    sd[i-1,:] = np.std(data[indexes,:],axis=0)
    
    
#Errorbars with standard deviation
species = np.array(['setosa','versicolor','virginica'])
features = np.array(header[:-1].astype("U"))
x = np.arange(len(features))

fig, ax = plt.subplots()
for i in labelsUn:
    ax.errorbar(x, average[i-1,:], sd[i-1,:], marker="o", label=species[i-1]) 

#Aesthetics    
ax.legend(loc="upper right")    
ax.set_xlabel("features", fontsize=14, fontweight='bold')
ax.set_ylabel("mean +/- sd", fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(features, rotation=45)
fig.tight_layout()  #make sure that the axes labels fit the figure


#Boxplots (1)-----------------------------------------------------
data0 = [12, 10, 100, 11, 3, 20]
print("data : ", data)  
print("Q1 quantile of data : ", np.quantile(data0, .25)) 
print("Q2 quantile of data : ", np.quantile(data0, .50)) 
print("Q3 quantile of data : ", np.quantile(data0, .75)) 
print("median of data : ", np.median(data0)) 
print("mean of data : ", np.mean(data0)) 
fig, ax = plt.subplots()
ax.boxplot(data0)

#Boxplots (2)-----------------------------------------------------
outliers = dict(marker='+', markerfacecolor='black')
medians = dict(linewidth=2)
boxes = np.array([dict(facecolor='r',color='r'),
                  dict(facecolor='g',color='g'), 
                  dict(facecolor='b',color='b')])
    
mylegend = [plt.scatter([0],[0],facecolor='r', edgecolor='r', label=species[0]),
            plt.scatter([0],[0],facecolor='g', edgecolor='g', label=species[1]),
            plt.scatter([0],[0],facecolor='b', edgecolor='b', label=species[2])]
plt.close("all") #make sure that no figure is generated

x = -7
step = 5
fig, ax = plt.subplots()

for j in range(len(features)): #for each feature...
    x+= 7
    for i in labelsUn:         #for each category...
        indexes = np.reshape(labels==i,nrows)
        temp = data[indexes,j]
        ax.boxplot(temp, positions=[x],
                   widths=2,
                   patch_artist=True,
                   medianprops=medians,
                   boxprops=boxes[i-1],
                   flierprops=outliers)
        x+= step

ax.set_title("iris data set", fontsize=13, fontweight='bold')
ax.set_ylabel("values", fontweight='bold')
ax.set_xticks(np.arange(step,x,22))
ax.set_xticklabels(features, fontweight='bold', rotation=45)
ax.legend(handles=mylegend)
fig.tight_layout()  #make sure that the axes labels fit the figure
plt.show()


