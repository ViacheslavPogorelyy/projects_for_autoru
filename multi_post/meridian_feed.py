#!/usr/bin/env python
# coding: utf-8

# In[18]:


import xml.etree.ElementTree as ET
import lxml.html as html
from pandas import DataFrame
import requests as r
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from lxml import objectify


# In[19]:


URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'


# In[20]:


from lxml import objectify
xml = objectify.parse(URL)
root = xml.getroot()


# In[137]:


print(root.getchildren()[1].getchildren()[7].getchildren())
print(root.getchildren()[1].getchildren()[9].getchildren())
print(root.getchildren()[1].getchildren()[10].getchildren())


# data1=[]
# for i in range(len(root.getchildren())):
#     idd = root.getchildren()[i].getchildren()[0]
#     title = root.getchildren()[i].getchildren()[1]
#     oem = root.getchildren()[i].getchildren()[2]
#     manu = root.getchildren()[i].getchildren()[3]
#     des = root.getchildren()[i].getchildren()[4]
#     is_new = root.getchildren()[i].getchildren()[5]
#     price = root.getchildren()[i].getchildren()[6]
#     avia = root.getchildren()[i].getchildren()[7].getchildren()
#     url = root.getchildren()[i].getchildren()[8]
#     prop = root.getchildren()[i].getchildren()[9].getchildren()
#     images = root.getchildren()[i].getchildren()[10].getchildren()
#     comp = root.getchildren()[i].getchildren()[11].getchildren())

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
    


# In[108]:


len(comp)


# In[85]:


data=[]
for i in range(len(root.getchildren())):
    data.append([child.text for child in root.getchildren()[i].getchildren()])


# In[86]:


data


# In[ ]:




