#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


data = pd.read_csv("ratings.csv")


# In[7]:


shape = data.shape


# In[8]:


print("Shape = {}".format(shape))


# In[9]:


id_dif = pd.DataFrame(data)


# In[13]:


uni_id = pd.unique(id_dif.movieId)


# In[11]:


print(f"Unique values present in User id column are: {uni_id}")


# In[17]:


df=pd.DataFrame("ratings.csv")


# In[18]:


answer=data['rating'].max()


# In[19]:


print(answer)


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


plt.hist(data, bins=30)


# In[24]:


plt.xlabel('movieId')
plt.ylabel('rating')


# In[25]:


plt.show()


# In[26]:


data.columns


# In[27]:


data['rating'],max


# In[28]:


data['rating'].max()


# In[30]:


data['rating'].max()==data['rating'].max()


# In[33]:


print(data[data['rating'].max()==data['rating'].max()])


# In[34]:


data.info


# In[35]:


data.describe


# In[37]:


data.groupby('movieId')['rating'].mean()


# In[38]:


data.groupby('79132')['rating'].mean()


# In[39]:


data.groupby('movieId')['rating'].mean().sort_values()


# In[40]:


data.groupby('movieId')['rating'].mean(ascending=False)


# In[41]:


data.groupby('movieId')['rating'].mean().sort_values(ascending=False)


# In[46]:


largedata=data.nlargest(20,'rating')


# In[47]:


data.groupby(largedata)


# In[ ]:




