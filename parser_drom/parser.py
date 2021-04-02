#!/usr/bin/env python
# coding: utf-8

# In[197]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 


# In[198]:


URL='https://baza.drom.ru/company/dokavto74'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[199]:


title = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item-content__subject-container'}):
    title.append(row.text)


# In[200]:


price = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('span', attrs = {'class':'price-per-quantity__price'}):
    price.append(row.text)


# In[201]:


manufacture = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item__annotation-row manufacturer'}):
    manufacture.append(row.text)


# In[202]:


img = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('a', attrs = {'href':'/krasnodar/sell_spare_parts/oblicovka-rychaga-akpp-kia-rio-3-2017-846504y300wk-sedan-1.6-g4fc-123-l-s-g6979842327.html'}):
    img.append(row.text)


# In[203]:


img


# In[204]:


feed = pd.DataFrame()
new = pd.Series(manufacture)
feed['title'] = title
feed['price'] = price
feed['manufacture'] = new
#feed['manufacture'] = manufacture


# In[205]:


feed['OEM']= feed['title'].str.split('[').str[1].str.split(']').str[0][:50]


# In[206]:


feed['category']= feed['title'].str.split(' ').str[0].str.split('[').str[0][:50]


# In[207]:


feed['price'] = feed['price'].str.replace('₽', '')


# In[208]:


pd.set_option('display.max_colwidth', -1)


# In[209]:


display(feed)


# In[210]:


import re


# In[211]:


result = re.findall(r'\b([A-Z][A-Za-z]+)', feed['title'][6])
print(result)


# In[212]:


result = re.findall(r'\b[а-яА-ЯёЁ]+', feed['title'][1] )
print(result)


# In[213]:


result = re.split(r'\b[а-яА-ЯёЁ]+', feed['title'][5], maxsplit=0)
print(result)


# In[214]:


result


# In[215]:


k = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('img'):
    k.append(row)


# In[216]:


k


# In[217]:


soup.find_all('img')


# In[ ]:




