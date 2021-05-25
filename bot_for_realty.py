#!/usr/bin/env python
# coding: utf-8

# In[202]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import csv
import io
import urllib.request
import schedule 
import time
from prettytable import PrettyTable


# In[203]:


import telebot


# In[204]:


bot = telebot.TeleBot('1884501099:AAGG33pv_ZkikRHYGDHYXMX9qps-qgUIe7o')


# In[205]:


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# In[206]:


df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv')


# In[207]:


key = df[['Названия строк', 'Сумма по полю Дней с новой ценой']]


# In[208]:


df = key[key['Сумма по полю Дней с новой ценой'] >= 10].reset_index()
df = df.drop(['index'], axis = 1)


# In[209]:


mytable = PrettyTable()


# In[210]:


mytable.field_names = ["Ссылка на оффер", "Дни с  новой ценой"]
# добавление данных по одной строке за раз
for i in range(len(df)):
    mytable.add_row([df['Названия строк'][i], df['Сумма по полю Дней с новой ценой'][i]])
# вывод таблицы в терминал


# In[211]:


mytable.align["Ссылка на оффер"] = "l"
mytable.align["Сумма с новой ценой"] = "l"
print(mytable)


# In[212]:


#Row_list =[]
#for i in range((df.shape[0])):
    #Row_list.append(list(df.iloc[i, :]))


# In[251]:


bot.send_message(-1001217016361, ggg, disable_web_page_preview = True)


# In[128]:


#for row in Row_list:
    #t = ('{:} {: >12}'.format(row[0], row[1]))
    #bot.send_message(-1001217016361, t, disable_web_page_preview = True)
    #time.sleep(3)


# In[199]:


bot.remove_webhook()


# In[114]:


bot.polling(none_stop=True, interval=0)


# In[306]:


ggg = PrettyTable(header = True, border = False, min_table_width = 80,padding_width = 0,right_padding_width = 0)


# In[307]:


ggg.field_names = ["Ссылка на оффер", "Дни с  новой ценой"]
# добавление данных по одной строке за раз
for i in range(len(df)):
    ggg.add_row([df['Названия строк'][i], df['Сумма по полю Дней с новой ценой'][i]])


# In[308]:


ggg.align["Ссылка на оффер"] = "l"
ggg.align["Сумма с новой ценой"] = "r"


# In[340]:


bot.send_message(-1001217016361, text="`ggg`", disable_web_page_preview = True, parse_mode= 'Markdown')


# In[341]:


print(ggg)


# In[ ]:




