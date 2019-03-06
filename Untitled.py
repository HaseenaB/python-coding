#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


x=pd.DataFrame({"Name":["Haseena","Thariq","Thabeena"],"Age":[27,33,2],"City":["Erode","Salem","Erode"]})


# In[3]:


x


# In[4]:


x['Name'] is x.Name


# In[6]:


y=pd.read_csv("E:\StudentsPerformance.csv")


# In[7]:


y


# In[8]:


y.loc[0:100,"gender":"lunch"]


# In[12]:


y.loc[1:50,["gender","math score","writing score"]]


# In[ ]:




