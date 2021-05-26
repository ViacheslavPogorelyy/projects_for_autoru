#!/usr/bin/env python
# coding: utf-8

# In[177]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import csv
import io
import urllib.request
import time
from prettytable import PrettyTable
import telebot


# In[178]:


bot = telebot.TeleBot('Secret')


# In[179]:


df = pd.read_csv('Secret-2')


# In[180]:


df


# In[181]:


df = df[['статус', 'ID объявления Яндекс', 'Адрес ', 'Дней с новой ценой']]


# In[182]:


data = df.loc[df['Дней с новой ценой'].isin([10,15,20,25,30])]
data = data.query('статус == "Нет"').reset_index()
data = data.drop(['index'], axis = 1)


# In[183]:


data


# In[184]:


Row_list =[]
for i in range((data.shape[0])):
    Row_list.append(list(data.iloc[i, :]))


# In[185]:


summ = 'У нас в базе {:} квартир с датой обновления цены более 10 дней'


# In[186]:


count = df.loc[df['Дней с новой ценой'] >= 10]
count = count.query('статус == "Нет"').reset_index()
count = count.drop(['index'], axis = 1)


# In[187]:


count = len(count['Дней с новой ценой'])


# In[188]:


if len(Row_list) > 0:
    for row in Row_list:
        t = ('Квартира по адресу: {:}, уже {: >2} дней в экопозиции. {: >2}'.format(row[2], row[3], row[1]))
        bot.send_message(-1001217016361, t, disable_web_page_preview = True, parse_mode = 'Markdown')
        time.sleep(3)
else:
    bot.send_message(-1001217016361, summ.format(count), disable_web_page_preview = True, parse_mode = 'Markdown')


# In[ ]:




