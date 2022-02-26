#!/usr/bin/env python
# coding: utf-8

# # Creating Bars
# with pyplot , bar() function can be useful to daw bar graphs

# In[1]:


#draw 4 bar graphs
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()


# The bar() function takes arguments that describes the layout of the bars.
# 
# The categories and their values represented by the first and second argument as arrays.

# In[2]:


x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)


# In[6]:


#HORIZONTAL BARS
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()


# In[7]:


#BAR COLOUR
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()


# In[8]:


#BAR WIDTH
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

