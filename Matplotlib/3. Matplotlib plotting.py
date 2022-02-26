#!/usr/bin/env python
# coding: utf-8

# # Matplotlib plotting
# plotting X and Y points
# the Plot() function is used to draw in a graph from point to point.
# It needs 2 parameters 
# parameter1 is for x-axis and parameter 2 for y axis

# # Q1. Draw a line in a diagram from position (1, 3) to position (8, 10)

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints)
plt.show()


# # Q2. Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

# In[6]:


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# # Q3. Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

# In[7]:


xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# # Q4. Plotting without X-Points

# In[8]:


ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()


# The x-points in the example above is [0, 1, 2, 3, 4, 5].
