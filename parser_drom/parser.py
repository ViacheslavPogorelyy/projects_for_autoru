#!/usr/bin/env python
# coding: utf-8

# In[217]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r


# In[218]:


URL='https://baza.drom.ru/company/dokavto74/'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[219]:


title = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item-content__subject-container'}):
    title.append(row.text)


# In[220]:


price = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('span', attrs = {'class':'price-per-quantity__price'}):
    price.append(row.text)


# In[221]:


manufacture = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item__annotation-row manufacturer'}):
    manufacture.append(row.text)


# In[222]:


feed = pd.DataFrame()


# In[223]:


text = r.get('https://baza.drom.ru/company/dokavto74/').text
k = re.findall(r'(https://static.baza.drom.ru/v/+\d{13}\D\w{5})', text)
img = pd.DataFrame(data = k, columns = ['img'])
img = img.drop_duplicates(subset=['img']).reset_index()


# In[224]:


feed['title'] = title
feed['price'] = price
feed['price'] = feed['price'].str.replace('₽', '')
feed['manufacture'] = pd.Series(manufacture)
feed['OEM']= feed['title'].str.split('[').str[1].str.split(']').str[0][:50]
feed['category']= feed['title'].str.split(' ').str[0].str.split('(').str[0][:50]
feed['image'] = img['img']


# In[225]:


pd.set_option('display.max_colwidth', -1)


# In[226]:


feed['category']= feed['title'].str.split(' ').str[0].str.split('(').str[0][:50]


# In[227]:


new = [] # Список, в котором хранятся названия запчастей
for i in range(len(feed['title'])):
    k = re.findall(r'\b[a-zA-Z]+.\b[a-zA-Z]+.\w+', feed['title'][i]) + re.findall(r'\d{4}–\d{4}', feed['title'][i])  
    new.append(k)

    
df12 = pd.DataFrame(data=new, columns=['lemmas', 'data'])


# In[228]:


feed['compatibility'] = df12['lemmas'] + " " + df12['data']


# In[229]:


feed


# In[230]:


feed.to_excel("feed.xlsx")


# In[ ]:




