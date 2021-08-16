#!/usr/bin/env python
# coding: utf-8

# In[20]:


import xml.etree.ElementTree as ET
import lxml.html as html
from pandas import DataFrame
import requests as r
import requests 
from bs4 import BeautifulSoup
import pandas as pd


# In[140]:


URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[141]:


image = []
for row in soup.find_all('images'):
    for row1 in row.find_all('image'):
        image.append(row1)


# In[142]:


df = pd.DataFrame(image, columns = ['link'])
dublicate = df['link'].value_counts()
dublicate = dublicate[dublicate > 1].reset_index()
bad_link = dublicate['index'].tolist()


# In[143]:


bad_link[48]


# In[153]:


new = []
for row in soup.find_all('images'):
        new.append(row)
    


# In[155]:


soup


# In[156]:


title = []
for row in soup.find_all('title'):
    title.append(row)    


# In[164]:


part = []
for row in soup.find_all('part'):
    part.append(row) 


# In[174]:


data = pd.DataFrame(columns = ['title'])


# In[178]:


title = []
for i in range(len(part)):
    for row in part[i].find_all('title'):
        title.append(row)


# In[179]:


part_number = []
for i in range(len(part)):
    for row in part[i].find_all('part_number'):
        part_number.append(row)


# In[181]:


len(part_number)


# In[ ]:




