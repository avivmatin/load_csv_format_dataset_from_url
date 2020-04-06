#!/usr/bin/env python
# coding: utf-8

# In[15]:


## STEP-1 load csv format dataset from url (.csv) by first define the url link 

url = 'https://raw.githubusercontent.com/ryanleeallred/datasets/master/Ames%20Housing%20Data/train.csv'


# In[14]:


## STEP-2 read the defined csv dataset in dataframe format

df1 = pd.read_csv(url)


# In[16]:


## STEP-3 print first 5 to see the dataframe works.

df1.head()


# In[ ]:




