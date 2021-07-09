#!/usr/bin/env python
# coding: utf-8

# In[124]:


import os, os.path
import glob
import shutil
import csv
import datetime
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET


# In[125]:


now = datetime.datetime.now()


# In[126]:


day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
microsecond = str(now.microsecond)


# In[127]:


csv_n = 'https://docs.google.com/spreadsheets/d/1FLgQtch4aZWjdVnRYh_ts9DReIS0gp2LvUyzt7E8XXk/export?format=csv'


# In[128]:


df = pd.read_csv(csv_n)


# In[129]:


df 


# In[130]:


#auto_ru = '<?xml version="1.0" encoding="utf-8"?>'


# In[131]:


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
compatibility = ET.SubElement(part, 'compatibility')
car = ET.SubElement(compatibility, 'compatibility')


# In[133]:


for i in range(len(df['id'])):
    title.text = df['title'][i]
    description.text = df['description'][i]
    price.text = df['price'][i]
    isAvailable.text = 'True'
    image.text = df['images'][i]
    is_new = df['is_new'][i]
    car.text = df['compatibility'][7]
    part_number.text = 'de44s25'
    store.text = '333981411'
    offer_url.text = 'http://sklad-fotki.ru/files/part23343'


# In[134]:


tree = ET.ElementTree(parts)
tree.write("sample.xml")


# In[ ]:




