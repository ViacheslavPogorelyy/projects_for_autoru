#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


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


# In[12]:


feed = pd.DataFrame()


# part
# id
# title
# part_number
# manufacturer
# description
# is_new
# price
# availability
# isAvailable
# offer_url
# properties
# property
# images
# image
# image
# image
# image
# compatibility
# car

# In[20]:


feed['part'] = []
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
for i in range(len(root.getchildren())):
    g = root.getchildren()[i].getchildren()
    part = []
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
    feed['part'].append(part)
    feed['id'].append(idd)
    feed['title'].append(title)
    feed['part_number'].append(part_number)
    feed['manufacturer'].append(manufacturer)
    feed['description'].append(description)
    feed['is_new'].append(is_new)
    feed['price'].append(price)
    feed['availability'].append(availability)
    feed['offer_url'].append(offer_url)
    feed['properties'].append(properties)
    feed['images'].append(images)
    feed['compatibility'].append(compatibility)
    for y in range(len(g)):
        if g[y].tag == 'part':
            part.append(g[y])
            break
        if g[y].tag == 'id':
            idd.append(g[y])
            break
        if g[y].tag == 'title':
            title.append(g[y])
            break
        if g[y].tag == 'part_number':
            part_number.append(g[y])
            break
        if g[y].tag == 'manufacturer':
            manufacturer.append(g[y])
            break
        if g[y].tag == 'description':
            description.append(g[y])
            break
        if g[y].tag == 'is_new':
            is_new.append(g[y])
            break
        if g[y].tag == 'price':
            price.append(g[y])
            break
        if g[y].tag == 'availability':
            availability.append(g[y].getchildren())
            break
        if g[y].tag == 'offer_url':
            offer_url.append(g[y])
            break
        if g[y].tag == 'properties':
            properties.append(g[y])
            break
        if g[y].tag == 'images':
            images.append(g[y].getchildren())
            break
        if g[y].tag == 'compatibility':
            compatibility.append(g[y].getchildren())
            break


# In[25]:


feed = pd.DataFrame()


# In[10]:


ttt = []
for i in range(len(root.getchildren())):
    g = root.getchildren()[i].getchildren()
    new = []
    ttt.append(new)
    for y in range(len(g)):
        if g[y].tag == 'availability' or g[y].tag == 'properties' or g[y].tag == 'images' or g[y].tag == 'compatibility':
            new.append(g[y].getchildren())
        else:
            new.append(g[y])


# In[11]:


ttt


# In[9]:


ttt1 = []
for i in range(len(root.getchildren())):
    g = root.getchildren()[i].getchildren()
    new1 = []
    ttt1.append(new1)
    for y in range(len(g)):
        if g[y].tag == 'images':
            new1.append(g[y].getchildren())
        else:
            pass


# In[249]:


ttt1[2][1]


# In[ ]:





# In[273]:


len(bad_link)


# In[ ]:


for i in range(len(ttt1)):
    for x in range(len(bad_link)):
        print(bad_link[x])
        print(ttt1[i][0])
        if ttt1[i][0] == bad_link[x]:
            ttt1[i][0].remove(bad_link[x])
        


# In[234]:


ttt[1]


# In[174]:


len(spisok)


# In[173]:


for i in range(len(root.getchildren()):
    spisok.getchildren()


# In[131]:


root.find('image')


# In[132]:


sectionList = root.findall('image')


# In[137]:


data=[]
for i in range(len(root.getchildren())):
    data.append([child.text for child in root.getchildren()[i].getchildren()])


# In[138]:


data


# In[159]:


spisok[8][8].tag


# In[167]:


root.iterchildren(reversed=False)


# In[136]:


spisok[1][9]


# In[125]:


spisok[1][8] 


# In[126]:


spisok[1][8].getchildren()


# In[127]:


spisok[1][8] = (spisok[1][8].getchildren()).remove(bad_link[12])


# In[105]:


ttt = test.getchildren().remove(bad_link[1])


# In[50]:


ttt = spisok[1].remove('https://euzp.ru/p5')


# In[8]:


root.findtext('x', default='Huh?')


# In[47]:


walkAll = root.getiterator()


# In[48]:


for elt in walkAll:
    print(elt.tag)


# In[ ]:


for kid in spisok[1]:
        print(kid.tag)


# In[25]:


spisok[1].getiterator(tag='title')


# In[2]:


#URL='http://baz-on.ru/export/c391/6d1e4/autoru-piter.xml'
#req = requests.get(URL) # GET-запрос
#soup = BeautifulSoup(req.text, 'xml')


# In[5]:


#soup


# In[6]:


#image = []
#for row in soup.find_all('images'):
    #for row1 in row.find_all('image'):
        #image.append(row1)


# In[ ]:





# In[7]:


#df = pd.DataFrame(data = image, columns = ['link'])
#dublicate = df['link'].value_counts()
#dublicate = dublicate[dublicate > 1].reset_index()
#bad_link = dublicate['index'].tolist()


# In[33]:


ser = pd.Series(image)


# In[34]:


dublicate = ser.value_counts()


# In[35]:


dublicate = dublicate[dublicate > 1].reset_index()
bad_link = dublicate['index'].tolist()


# In[36]:


bad_link

