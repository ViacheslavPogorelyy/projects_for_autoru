#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import csv
import io
import urllib.request


# In[2]:


import telebot


# In[3]:


bot = telebot.TeleBot('1884501099:AAGG33pv_ZkikRHYGDHYXMX9qps-qgUIe7o')


# In[4]:


bot


# In[5]:


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот, которые будет помогать сервису стать лучше')


# In[6]:


bot.polling(none_stop=True, interval=0)


# In[23]:


#url = 'https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv'

#response = urllib.request.urlopen(url)


#with io.TextIOWrapper(response, encoding='utf-8') as f:
    #reader = csv.reader(f)

    #for row in reader:
        #print(row)


# In[21]:


df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv')


# In[22]:


df


# In[ ]:




