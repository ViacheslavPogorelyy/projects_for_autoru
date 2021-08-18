#!/usr/bin/env python
# coding: utf-8

# In[7]:


import xml.etree.ElementTree as ET
import lxml.html as html
from pandas import DataFrame
import requests as r
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from lxml import objectify


# In[5]:


URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'


# In[6]:


from lxml import objectify
xml = objectify.parse(URL)
root = xml.getroot()


# In[8]:


spisok=[]
for i in range(len(root.getchildren())):
    spisok.append(root.getchildren()[i].getchildren())


# In[49]:


root.getchildren()[1].getchildren()


# In[6]:


data=[]
for i in range(len(root.getchildren())):
    data.append([child.text for child in root.getchildren()[i].getchildren()])


# In[7]:


data


# In[5]:


print(root.getchildren()[1].getchildren()[7].getchildren())
print(root.getchildren()[1].getchildren()[9].getchildren())
print(root.getchildren()[1].getchildren()[10].getchildren())


# In[103]:


avia = []
prop = []
images = []
comp = []
for i in range(len(root.getchildren())):
    try:
        av = root.getchildren()[i].getchildren()[7].getchildren()
        pr = root.getchildren()[i].getchildren()[9].getchildren()
        im = root.getchildren()[i].getchildren()[10].getchildren()
        com = root.getchildren()[i].getchildren()[11].getchildren()
    except:
        com = None
    avia.append([av])
    prop.append([pr])
    images.append([im])
    comp.append([com])
    


# In[ ]:




