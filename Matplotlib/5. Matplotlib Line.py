#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Line
# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()


# In[2]:


#use a dashed line
plt.plot(ypoints, linestyle = 'dashed')


# # Line Color
# You can use the keyword argument color or the shorter c to set the color of the line:

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()


# # Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()


# In[5]:


#method 2
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

