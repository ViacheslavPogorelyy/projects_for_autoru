#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 


# In[53]:


URL='https://baza.drom.ru/company/dokavto74'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[54]:


title = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item-content__subject-container'}):
    title.append(row.text)


# In[55]:


price = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('span', attrs = {'class':'price-per-quantity__price'}):
    price.append(row.text)


# In[56]:


manufacture = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('div', attrs = {'class':'bull-item__annotation-row manufacturer'}):
    manufacture.append(row.text)


# In[57]:


img = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('a', attrs = {'href':'/krasnodar/sell_spare_parts/oblicovka-rychaga-akpp-kia-rio-3-2017-846504y300wk-sedan-1.6-g4fc-123-l-s-g6979842327.html'}):
    img.append(row.text)


# In[58]:


img


# In[59]:


feed = pd.DataFrame()
new = pd.Series(manufacture)
feed['title'] = title
feed['price'] = price
feed['manufacture'] = new
#feed['manufacture'] = manufacture


# In[60]:


feed['OEM']= feed['title'].str.split('[').str[1].str.split(']').str[0][:50]


# In[61]:


feed['price'] = feed['price'].str.replace('₽', '')


# In[62]:


pd.set_option('display.max_colwidth', -1)


# In[63]:


feed['category']= feed['title'].str.split(' ').str[0].str.split('(').str[0][:50]


# In[64]:


import re


# In[65]:


result = re.findall(r'\b([а-яА-ЯёЁ]+)', feed['title'][11])
print(result)


# In[66]:


new = [] # Список, в котором хранятся названия запчастей
for i in range(len(feed['title'])):
    k = re.findall(r'\b[a-zA-Z]+.\b[a-zA-Z]+.\w+', feed['title'][i]) + re.findall(r'\d{4}–\d{4}', feed['title'][i])  
    new.append(k)

    
df12 = pd.DataFrame(data=new, columns=['lemmas', 'data'])


# In[67]:


feed['compatibility'] = df12['lemmas'] + " " + df12['data']


# In[68]:


display(feed)


# In[69]:


feed.to_excel("feed.xlsx")


# In[70]:


result = re.search(r'\b[a-zA-Z]+', feed['title'][1] )
print(result)


# In[71]:


result = re.split(r'\A[а-яА-ЯёЁ]+', feed['title'][33], maxsplit=0)
print(result)


# In[72]:


k = [] # Список, в котором хранятся названия запчастей
for row in soup.find_all('img'):
    k.append(row)


# In[73]:


k


# In[74]:


soup.find_all('img')


# In[75]:


result = re.findall(r'\d{4}–\d{4}', 'Фонарь задний (стоп сигнал) Toyota Mark II (X110) IX 2000–2002  [007B76817]')
print(result)


# In[ ]:




