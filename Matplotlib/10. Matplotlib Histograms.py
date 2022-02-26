#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Histograms

# A histogram is a graph showing frequency distributions.
# 
# It is a graph showing the number of observations within each given interval.

# # Create Histogram
# In Matplotlib, we use the hist() function to create histograms.
# 
# The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

# # Without Histogram

# In[9]:


import numpy as np

x = np.random.normal(170, 10, 250)

print(x)


# # With Histogram

# In[10]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

