#!/usr/bin/env python
# coding: utf-8

# In[50]:


import os, os.path
import glob
import shutil
import csv
import datetime
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET


# In[51]:


now = datetime.datetime.now()


# In[52]:


day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
microsecond = str(now.microsecond)


# In[53]:


csv_n = 'https://docs.google.com/spreadsheets/d/1FLgQtch4aZWjdVnRYh_ts9DReIS0gp2LvUyzt7E8XXk/export?format=csv'


# In[54]:


df = pd.read_csv(csv_n)


# In[55]:


df 


# In[56]:


#auto_ru = '<?xml version="1.0" encoding="utf-8"?>'


# In[57]:


parts = ET.Element('parts')
part = ET.SubElement(parts, 'part')
id_part = ET.SubElement(part, 'id')
title = ET.SubElement(part, 'title')
stores = ET.SubElement(part, 'stores')
store = ET.SubElement(stores, 'store')
part_number = ET.SubElement(part, 'part_number')
offer_url = ET.SubElement(part, 'offer_url')
manufacturer = ET.SubElement(part, 'manufacturer')
description = ET.SubElement(part, 'description')
is_new = ET.SubElement(part, 'is_new')
price = ET.SubElement(part, 'price')
availability = ET.SubElement(part, 'availability')
isAvailable = ET.SubElement(availability, 'isAvailable')
images = ET.SubElement(part, 'images')
image = ET.SubElement(images, 'image')


# In[58]:


tree = ET.ElementTree(parts)
tree.write("sample.xml")


# In[ ]:




