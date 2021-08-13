#!/usr/bin/env python
# coding: utf-8

# In[36]:


import xml.etree.ElementTree as ET
import lxml.html as html
from pandas import DataFrame
import requests as r
import requests 
from bs4 import BeautifulSoup
import pandas as pd


# In[37]:


URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[109]:


image = []
for row in soup.find_all('images'):
    for row1 in row.find_all('image'):
        image.append(row1)


# In[116]:


df = pd.DataFrame(image, columns = ['link'])
dublicate = df['link'].value_counts()
dublicate = dublicate[dublicate > 1].reset_index()
bad_link = dublicate['index'].tolist()


# In[147]:


new = []
for row in soup.find_all('images'):
    new.append(row)


# In[153]:


len(new)


# In[155]:


for i in range(20199):
    print(new[0])


# In[39]:


image = pd.Series(image)
drop_dublicated = image.drop_duplicates(False)


# In[40]:


drop_dublicated


# In[41]:


image


# In[6]:


image


# In[ ]:




