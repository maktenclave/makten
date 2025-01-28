#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
s1=a[2:6]
print(s1)


# In[3]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
s2=a[::2]
print(s2)


# In[4]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
s3=a[::-1]
print(s3)


# In[5]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
s=a[0:2,1:3]
print(s)


# In[6]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
s=a[::1,0:2]
print(s)


# In[7]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
s=a[:2,:1]
print(s)


# In[8]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
s=a[:,0]
print(s)


# In[9]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
s=a[0,:]
print(s)


# In[12]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
s=a[0:3:2]
print(s)


# In[17]:


import numpy as np
import array
a=array.array('i',[1,2,3,4,5])
print(a[0])
print(a[-1])


# In[21]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a[0,0])


# In[20]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a[2:5])


# In[31]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0,1])


# In[29]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a[a>2])


# In[30]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a[[1,3]])


# In[4]:


import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
r=np.hstack((a,b))
print(r)


# In[5]:


import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
r=np.vstack((a,b))
print(r)


# In[7]:


import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
r=np.dstack((a,b))
print(r)


# In[8]:


import numpy as np
a=np.array([1,2,3,4,5,6])
r=np.split(a,3)
print(r)


# In[10]:


import numpy as np
a=np.array([1,2,3,4,5])
r=np.array_split(a,3)
print(r)


# In[ ]:




