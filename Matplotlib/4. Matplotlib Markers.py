#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Markers
# we can use marker to emphasize each point with a specified marker:
# 

# # Q1. Mark each point with circle

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# In[2]:


#Marking point with star
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()


# # Format Strings fmt
# You can use also use the shortcut string notation parameter to specify the marker.
# 
# This parameter is also called fmt, and is written with this syntax:
# 
# marker|line|color

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')#inplace of o:r, we cn also use":","--"
plt.show()


# You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()


# # Marker Color
# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:

# In[6]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()


# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
