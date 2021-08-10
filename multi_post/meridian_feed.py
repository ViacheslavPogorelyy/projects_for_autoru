#!/usr/bin/env python
# coding: utf-8

# In[32]:


import xml.etree.ElementTree as ET
import lxml.html as html
from pandas import DataFrame
import requests as r
import requests 
from bs4 import BeautifulSoup 


# In[33]:


URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[34]:


soup


# In[46]:


image = []
for row in soup.find_all('images'):
    image.append(row)


# In[48]:


image[2]


# In[40]:


soup.find('images')


# In[ ]:




