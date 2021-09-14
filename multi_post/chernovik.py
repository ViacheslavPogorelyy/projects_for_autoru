#!/usr/bin/env python
# coding: utf-8

# In[92]:


import xml.etree.ElementTree as ET
import lxml.html as html
from pandas import DataFrame
import requests as r
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from pyparsing import *
from bs4.element import NavigableString
from lxml import objectify
import sys,os,xml.dom.minidom
import numpy as np


# In[38]:


URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'
xml = objectify.parse(URL)
root = xml.getroot()


# In[3]:


req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'xml')


# In[4]:


image = []
for row in soup.find_all('images'):
    for row1 in row.find_all('image'):
        image.append(row1)


# In[5]:


link = pd.Series(data = image)
dublicate = link.value_counts()
dublicate = dublicate[dublicate > 1].reset_index()
bad_link = dublicate['index'].tolist()


# In[6]:


for i in range(len(bad_link)):
    bad_link[i] = str(bad_link[i]).replace('<image>', '')
    bad_link[i] = bad_link[i].replace('</image>', '')


# In[7]:


bad_link


# In[33]:


feed = pd.DataFrame()

#feed['part'] = range(0,20122)


# In[85]:


feed['id'] = []
feed['title'] = []
feed['part_number'] = []
feed['manufacturer'] = []
feed['description'] = []
feed['is_new'] = []
feed['price'] = []
feed['availability'] = []
feed['offer_url'] = []
feed['properties'] = []
feed['images'] = []
feed['compatibility'] = []


# In[117]:


idd = []
title = []
part_number = []
manufacturer = []
description = []
is_new = []
price = []
availability = []
offer_url = []
properties = []
images = []
compatibility = []
for i in range(10):
    g = root.getchildren()[i].getchildren()
    rem = pd.Series(str(idd),index=np.arange(len(idd)))
    for y in range(len(g)):
        if g[y].tag == 'id':
            idd.append(g[y])
        if g[y].tag == 'title':
            title.append(g[y])
        if g[y].tag == 'part_number':
            part_number.append(g[y])
        if g[y].tag == 'manufacturer':
            manufacturer.append(g[y])
        if g[y].tag == 'description':
            description.append(g[y])
        if g[y].tag == 'is_new':
            is_new.append(g[y])
        if g[y].tag == 'price':
            price.append(g[y])
        if g[y].tag == 'availability':
            availability.append(g[y].getchildren())
        if g[y].tag == 'offer_url':
            offer_url.append(g[y])
        if g[y].tag == 'properties':
            properties.append(g[y].getchildren())
        if g[y].tag == 'images':
            images.append(g[y].getchildren())
        if g[y].tag == 'compatibility':
            compatibility.append(g[y].getchildren())


# In[ ]:




