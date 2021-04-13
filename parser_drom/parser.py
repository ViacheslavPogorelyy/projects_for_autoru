#!/usr/bin/env python
# coding: utf-8

# In[155]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np


# In[169]:


URL='https://baza.drom.ru/company/dokavto74?page=2'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[170]:


title = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item-content__subject-container'}):
    title.append(row.text)


# In[171]:


price = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('span', attrs = {'class':'price-per-quantity__price'}):
    price.append(row.text)


# In[172]:


manufacture = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item__annotation-row manufacturer'}):
    manufacture.append(row.text)


# In[173]:


img = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('a', attrs = {'href':'/krasnodar/sell_spare_parts/oblicovka-rychaga-akpp-kia-rio-3-2017-846504y300wk-sedan-1.6-g4fc-123-l-s-g6979842327.html'}):
    img.append(row.text)


# In[174]:


feed = pd.DataFrame()
feed['title'] = title
feed['price'] = price
feed['price'] = feed['price'].str.replace('₽', '')
feed['manufacture'] = pd.Series(manufacture)
feed['OEM']= feed['title'].str.split('[').str[1].str.split(']').str[0][:50]


# In[175]:


pd.set_option('display.max_colwidth', -1)


# In[176]:


feed['category']= feed['title'].str.split(' ').str[0].str.split('(').str[0][:50]


# In[177]:


#result = re.findall(r'\b([а-яА-ЯёЁ]+)', feed['title'][11])
#print(result)


# In[178]:


new = [] # Список, в котором хранятся названия запчастей
for i in range(len(feed['title'])):
    k = re.findall(r'\b[a-zA-Z]+.\b[a-zA-Z]+.\w+', feed['title'][i]) + re.findall(r'\d{4}–\d{4}', feed['title'][i])  
    new.append(k)

    
df12 = pd.DataFrame(data=new, columns=['lemmas', 'data'])


# In[179]:


feed['compatibility'] = df12['lemmas'] + " " + df12['data']


# In[180]:


display(feed)


# In[181]:


feed.to_excel("feed.xlsx")


# In[182]:


k = [] # Список, в котором хранятся ссылки на миниатюры фото запчастей
for row in soup.find_all('img'):
    k.append(row)


# In[183]:


k


# In[130]:


result = re.findall(r'\d{4}–\d{4}', 'Рычаг стояночного тормоза Ford Focus (III) III (2010–2015) [BV612780CE]')
print(result)


# In[ ]:




