#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Pyplot
# most of the Matplotlib utilities lies under the pyplot submodule and are ususally imported under plt alias

# In[1]:


import matplotlib.pyplot as plt


# 
# pyplot can be referred as plt in the upcoming code

# # Q1. Draw a line in a diagram from position (0,0) to position (6,250): 

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()


# We just located xpoints and ypoints which is xaxis and yaxis and used plot function to plot them.
