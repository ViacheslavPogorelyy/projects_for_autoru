#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import urllib3
urllib3.disable_warnings()


# In[12]:


URL='https://www.avito.ru/shops/rostov-na-donu/nedvizhimost'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# In[13]:


soup


# In[41]:


for link in soup.find_all('a'):
        count_pages = link.get('href')
        
num = re.findall(r'(p=\d+)', count_pages)

last = num[0].replace('p=', '')
last = int(last)


# In[5]:


city = URL.replace('https://www.avito.ru/shops/', '')
city = re.findall(r'(\S+\W+)', city)
city = city[0].replace('/', '')


# In[6]:


full_link = city+'?page_from=from_shops_list'


# In[18]:


for_title = []
for_count = []
for_result = []
for i in range(1, last+1):
    url_link = URL+'?p=' + str(i)
    response = requests.get(url_link, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    for_text = r.get(url_link).text
    result = re.findall(r'(\w+\S{1}\W+rostov-na-donu+\W+page_from=from_shops_list)', for_text)
    for_result.append(result)
    for row in soup.find_all('h3', attrs = {'class': 't_s_h3'}):
        for_title.append(row.text)
    for row_1 in soup.find_all('div', attrs = {'class': 't_s_items'}):
        for_count.append(row_1.text)


# In[37]:


print(len(for_result[0]))
print(len(for_result[1]))
print(len(for_result[2]))
print(len(for_result[3]))


# In[26]:


for_elenemt = []
for i in range(len(for_result)):
    for element in for_result[i]:
        for_elenemt.append(element)
        
result = pd.DataFrame(data = for_elenemt, columns = ['link'])
result = result.drop_duplicates(subset=['link']).reset_index()


# In[27]:


result


# In[91]:


just = '\w+\S{1}\W+'


# In[92]:


reg_exp = just+full_link
#reg_exp = r'w+\S{1\W+{}'.format(full_link)

#full_link
result = re.findall(reg_exp, for_text)


# In[30]:


etalon = pd.DataFrame()


# In[28]:


links = []
for i in result['link']:
    id_avito = "https://www.avito.ru/{}".format(i)
    links.append(id_avito)


# In[33]:


len(links)


# In[14]:


etalon['title'] = for_title
etalon['title'] = etalon['title'].str.replace('\n\n ', '')
etalon['title'] = etalon['title'].str.replace('\n', '')
etalon['count'] = for_count
etalon['count'] = etalon['count'].str.replace('\n\n ', '')
etalon['count'] = etalon['count'].str.replace('\n', '')
#etalon['links'] = links


# In[208]:


etalon


# In[292]:


for_text = r.get(url_link).text
result = re.findall(r'(\w+\S{1}\W+rostov-na-donu+\W+page_from=from_shops_list)', for_text)

