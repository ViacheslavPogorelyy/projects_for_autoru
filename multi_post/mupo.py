#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os, os.path
import glob
import shutil
import csv
import datetime
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET


# In[30]:


now = datetime.datetime.now()


# In[31]:


day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
microsecond = str(now.microsecond)


# In[32]:


csv_n = 'https://docs.google.com/spreadsheets/d/1FLgQtch4aZWjdVnRYh_ts9DReIS0gp2LvUyzt7E8XXk/export?format=csv'


# In[33]:


df = pd.read_csv(csv_n)


# In[35]:


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


# In[43]:


for i in range(len(df['id'])):
    title.text = df['title'][i]
    description.text = df['description'][i]
    price.text = df['price'][i]
    isAvailable.text = 'True'
    image.text = df['images'][i]
    is_new = df['is_new'][i]
    car.text = df['compatibility'][i]
    part_number.text = df['part_number'][i]
    manufacturer.text = df['manufacturer'][i]
    offer_url.text = df['url'][i]


# In[42]:


tree = ET.ElementTree(parts)
#mydata = ET.tostring(parts, encoding="utf-8", method="xml")
tree.write("sample.xml", encoding='utf8')


# In[63]:


#def func(row):
    #xml = ['<part>']
    #for field in row.index:
        #xml.append('  <{0}>{1}</field>'.format(field, row[field]))
    #xml.append('</parts>')
    #return '\n'.join(xml)


# In[64]:


#t = '\n'.join(df.apply(func, axis=1))


# In[ ]:




