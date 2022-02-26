#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Pie Charts

# # Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:

# In[11]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 


# # Labels
# Add labels to the pie chart with the label parameter.
# 
# The label parameter must be an array with one label for each wedge:

# In[12]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()


# # Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
# 
# The startangle parameter is defined with an angle in degrees, default angle is 0:

# In[14]:


#Start the first wedge at 90 degrees:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 


# # Explode
# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
# 
# The explode parameter, if specified, and not None, must be an array with one value for each wedge.

# In[15]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 


# # colours

# In[16]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 


# # Legend
# To add a list of explanation for each wedge, use the legend() function:

# In[17]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

