#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, os.path
import glob
import shutil
import csv
import datetime
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET


# In[2]:


csv_n = 'https://docs.google.com/spreadsheets/d/1FLgQtch4aZWjdVnRYh_ts9DReIS0gp2LvUyzt7E8XXk/export?format=csv'


# In[3]:


df = pd.read_csv(csv_n)
df


# In[4]:


df['compatibility'] = df['compatibility'].str.split(';')
df['images'] = df['images'].str.split(';')


# In[5]:


parts = ET.Element('parts')
for i in range(len(df['id'])):
    part = ET.SubElement(parts, 'part')
    id_part = ET.SubElement(part, 'id')
    title = ET.SubElement(part, 'title')
    title.text = df['title'][i]
    stores = ET.SubElement(part, 'stores')
    store = ET.SubElement(stores, 'store')
    part_number = ET.SubElement(part, 'part_number')
    part_number.text = df['part_number'][i]
    offer_url = ET.SubElement(part, 'offer_url')
    offer_url.text = df['url'][i]
    manufacturer = ET.SubElement(part, 'manufacturer')
    manufacturer.text = df['manufacturer'][i]
    description = ET.SubElement(part, 'description')
    description.text = df['description'][i]
    is_new = ET.SubElement(part, 'is_new')
    is_new.text = df['is_new'][i]
    price = ET.SubElement(part, 'price')
    price.text = df['price'][i]
    availability = ET.SubElement(part, 'availability')
    isAvailable = ET.SubElement(availability, 'isAvailable')
    isAvailable.text = df['is_available'][i]
    images = ET.SubElement(part, 'images')
    for y in range(len(df['images'][i])):
        image = ET.SubElement(images, 'image')
        image.text = df['images'][i][y]
    compatibility = ET.SubElement(part, 'compatibility')
    for num in range(len(df['compatibility'][i])):
        car = ET.SubElement(compatibility, 'car')
        car.text = df['compatibility'][i][num]
    tree = ET.ElementTree(parts)


# In[6]:


tree = ET.ElementTree(parts)
tree.write("sample.xml", encoding='utf8')

