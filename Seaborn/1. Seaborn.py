#!/usr/bin/env python
# coding: utf-8

# # Visualize Distributions with seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import seaborn as sns


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()


# # Plotting a Distplot Without the Histogram

# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()


# We will be using: sns.distplot(arr, hist=False) to visualize random distributions in this tutorial.
