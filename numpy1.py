#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])
print("\nOne dimensional array:\n",a)


# In[2]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("\nTwo dimensional array:\n",a)


# In[3]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nThree dimensional array:\n",a)


# In[4]:


import numpy as np
a=np.zeros((3,4))
print("\nArray withinall zeros:\n",a)


# In[5]:


import numpy as np
a=np.random.random((3,4))
print("\nRandom values:\n",a)


# In[6]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=a.reshape((3,4))
print("\nOriginal array:\n",a)
print("\nReshaped array:\n",b)


# In[7]:


import numpy as np
a=np.arange(0,51,5)
print("\nSequence array:\n",a)


# In[8]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.flatten()
print("\nOriginal array:\n",a)
print("\nFlatten array:\n",b)


# In[16]:


import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\nNo of dimensions:\n",a.ndim)


# In[19]:


import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\nShape of array:\n",a.shape)


# In[21]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("\nArray element:",a.dtype)


# In[24]:


import numpy as np
a=np.array([1,2,3,4,5,6])
l=len(a)
print("\nLenght of the array:",l)


# In[ ]:




