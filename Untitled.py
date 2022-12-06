#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[1]:


pip install numpy


# In[1]:


import pandas as pd
import numpy as np
ser=pd.Series()
print(ser)
data=np.array(['g','e','e','k','s'])
ser=pd.Series(data)
print(ser)


# In[5]:


info={'x':0.,'y':1.,'z':2.}
a=pd.Series(info)
print(a)


# In[13]:


a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[4,9,8,2,5,6])
index=(['x','y','z'])
print(a.dtype)
print(a.size)
print(b.dtype)
print(b.size)


# In[10]:


f=open("filehandling.txt","r")
print(f.read())


# In[18]:


f=open("filehandling.txt","r")
for x in f:
    print(x)


# In[19]:


f=open("filehandling.txt","r")
print(f.readline())
f.close()


# In[17]:


f=open("filehandling.txt","a")
f.write(". Now text is appended to file")
f.close()
f=open("filehandling.txt","r")
print(f.read())


# In[20]:


f=open("filehandling.text","w")
f.write("HI there")
f.close()
f=open("filehandling.text","r")
print(f.read())


# In[ ]:




