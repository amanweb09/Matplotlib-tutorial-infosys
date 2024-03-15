# -*- coding: utf-8 -*-
"""Matplotlib-continued.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13QmV0awj-653lKT4nTpbP1Pw78eA1YNQ

**Annotating the plot**
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(5,5))

ax = fig.add_subplot(111, polar=True)

r = np.arange(0,1,0.001)

theta = 2*np.pi*r
ind = 800

thisr, thistheta = r[ind], theta[ind]

ax.plot([thistheta], [thisr], 'o')

# annotating
ax.annotate("a-polar_annotation", xy=(thistheta, thisr))

"""**Drawing a line to connect 2 points of the chart**"""

x= [1,2,3,4,5]
y= [1,4,9,16, 25]
plt.plot(x, y, 'ro')  #ro indicates strong circles on the graph

def connect_points(x,y,p1,p2):
  x1, x2 = x[p1], x[p2]
  y1, y2 = y[p1], y[p2]
  plt.plot([x1,x2], [y1,y2])

connect_points(x,y, 0, 2)
connect_points(x,y, 2,3)

plt.axis('equal')
plt.show()

"""**adding text to plots**"""

plt.figure(figsize=(7,4))
ax = plt.subplot(111)

ax.annotate("Hello World", xy=(0.2, 0.2))
plt.show()

# create an arrow that points the text to a point
plt.figure(figsize=(7,4))
ax = plt.subplot(111)

# text placed at (0.6, 0.6) and points that (0.2, 0.2)
ax.annotate("Hello World",
            xy=(0.2, 0.2),
            xytext=(0.6, 0.6),
            arrowprops={"arrowstyle": "simple"})
plt.show()

"""**Boxplot**"""

data = pd.read_csv("bank-full.csv", sep=";")
data.head()

data.boxplot(column="balance", by="marital")

# method 2
fig, ax1 = plt.subplots()
ax1.set_title("Box Plot")
ax1.boxplot(data.balance)
plt.show()

"""**Creating 3D Charts**"""

from mpl_toolkits.mplot3d import axes3d
# from mpl_toolkits.basemap import Basemap

# to create 3d charts just pass projection=3d and 3 params i.e. x,y,z
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection="3d")

x=[10,20,30,40]
y=[55,65,75,85]
z=[2,4,6,8]
ax.scatter(x,y,z)
plt.show()

# adding colorbar to the chart
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection="3d")

x=[10,20,30,40]
y=[55,65,75,85]
z=[2,4,6,8]
scatter = ax.scatter(x,y,z, c=z)
cbar = plt.colorbar(scatter)
cbar.set_label("z")
plt.show()

"""**Contour Map**"""

def f(x,y):
  return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)

X, Y = np.meshgrid(x,y)
Z=f(X,Y)

fig = plt.figure()
ax = plt.axes(projection="3d")
# ax.countour3D(X,Y,Z, 50, cmap="binary")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')