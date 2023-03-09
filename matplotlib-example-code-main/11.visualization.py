# -*- coding: utf-8 -*-


# Import convention
import matplotlib.pyplot as plt

# We will also need
import numpy as np



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