#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import urllib3
urllib3.disable_warnings()


# In[173]:


URL='secret'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[175]:


for link in soup.find_all('a'):
        count_pages = link.get('href')
        
num = re.findall(r'(p=\d+)', count_pages)

last = num[0].replace('p=', '')
last = int(last)


# In[176]:


city = URL.replace('https://www.avito.ru/shops/', '')
city = re.findall(r'(\S+\W+)', city)
city = city[0].replace('/', '')


# In[177]:


full_link = city+'?page_from=from_shops_list'


# In[178]:


for_title = []
for_count = []
for_result = []
for i in range(1, last+1):
    url_link = URL+'?p=' + str(i)
    response = requests.get(url_link, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    for_text = r.get(url_link).text
    result = []
    for link in soup.find_all('a'):
        jam = (link.get('href'))
        if jam.endswith('page_from=from_shops_list'):
            for_result.append(jam)
        else: 
            t = 1 
    for row in soup.find_all('h3', attrs = {'class': 't_s_h3'}):
        for_title.append(row.text)
    for row_1 in soup.find_all('div', attrs = {'class': 't_s_items'}):
        for_count.append(row_1.text)


# In[179]:


result = pd.DataFrame(data = for_result, columns = ['link'])
result = result.drop_duplicates(subset=['link']).reset_index()


# In[180]:


etalon = pd.DataFrame()


# In[185]:


links = []
for i in result['link']:
    id_avito = "https://www.avito.ru{}".format(i)
    links.append(id_avito)


# In[186]:


etalon['title'] = for_title
etalon['title'] = etalon['title'].str.replace('\n\n ', '')
etalon['title'] = etalon['title'].str.replace('\n', '')
etalon['count'] = for_count
etalon['count'] = etalon['count'].str.replace('\n\n ', '')
etalon['count'] = etalon['count'].str.replace('\n', '')
etalon['links'] = links


# In[187]:


etalon


# In[189]:


etalon.to_excel("etalons.xlsx")


# In[ ]:




