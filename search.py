#!/usr/bin/env python
# coding: utf-8

# In[27]:


import json


# In[28]:


from user_and_pair import *


# In[29]:


from btree import *


# In[30]:


def btree_reload(file):
    f = open(file,)
    x = tree()
    data = json.load(f)
    for element in data:
        reborn = user(element['name'], element['age'], element['gender'], element['interest'], element['ideal_age'],
                      element['ideal_gender'], identity = element['id'])
        x.insert(reborn)
       # print(reborn.id)
    f.close()
    return x


# In[31]:


reborn_tree = btree_reload('storage.json')


# In[32]:


def btree_search(identity, binary_tree):
    return binary_tree.search(identity) 


# In[33]:


btree_search(794055, reborn_tree)


# In[ ]:




