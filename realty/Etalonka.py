#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import urllib3
urllib3.disable_warnings()


# In[2]:


URL='https://www.avito.ru/shops/rostov-na-donu/nedvizhimost'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


# Получаем все ссылки на странице и количество страниц с предложениями

# In[3]:


for link in soup.find_all('a'):
        count_pages = link.get('href')
        
num = re.findall(r'(p=\d+)', count_pages)

last = num[0].replace('p=', '')
last = int(last)


# Создаем цикл, где отдельно достаем наименованеи магазина, количество офферов и ссылки на магазин.

# In[4]:


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


# Избавляемся от дублей ссылок

# In[32]:


result = pd.DataFrame(data = for_result, columns = ['link'])
unique_link = result.drop_duplicates(subset=['link']).reset_index()


# Получаем послные кликабельные ссылки на магазин

# In[33]:


links = []
for i in unique_link['link']:
    id_avito = "https://www.avito.ru{}".format(i)
    links.append(id_avito)


# Создаем датафрейм, в котором у нас будут формироваться искомые данные

# In[34]:


etalon = pd.DataFrame()


# Форматируем столбцы Датафрейма с конечным результатом 

# In[35]:


etalon['title'] = for_title
etalon['title'] = etalon['title'].str.replace('\n\n ', '')
etalon['title'] = etalon['title'].str.replace('\n', '')
etalon['count'] = for_count
etalon['count'] = etalon['count'].str.replace('\n\n ', '')
etalon['count'] = etalon['count'].str.replace('\n', '')
etalon['links'] = links


# In[36]:


etalon


# In[37]:


etalon.to_excel("parts_etalons.xlsx")

