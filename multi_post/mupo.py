#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os, os.path
import glob
import shutil
import csv
import datetime
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET


# In[16]:


csv_n = 'https://docs.google.com/spreadsheets/d/1FLgQtch4aZWjdVnRYh_ts9DReIS0gp2LvUyzt7E8XXk/export?format=csv'


# In[17]:


df = pd.read_csv(csv_n)


# In[18]:


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
    image = ET.SubElement(images, 'image')
    image.text = df['images'][i]
    compatibility = ET.SubElement(part, 'compatibility')
    car = ET.SubElement(compatibility, 'car')
    car.text = df['compatibility'][i]
    tree = ET.ElementTree(parts)


# In[19]:


tree = ET.ElementTree(parts)
tree.write("sample.xml", encoding='utf8')

