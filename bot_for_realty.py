#!/usr/bin/env python
# coding: utf-8

# In[149]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import csv
import io
import urllib.request


# In[150]:


import telebot


# In[151]:


bot = telebot.TeleBot('1884501099:AAGG33pv_ZkikRHYGDHYXMX9qps-qgUIe7o')


# In[152]:


#@bot.message_handler(commands=['start'])
#def send_welcome(message):
    #bot.reply_to(message, f'Привет! Я бот, которые будет помогать сервису стать лучше')


# In[153]:


#bot.polling(none_stop=True, interval=0)


# In[154]:


#url = 'https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv'

#response = urllib.request.urlopen(url)


#with io.TextIOWrapper(response, encoding='utf-8') as f:
    #reader = csv.reader(f)

    #for row in reader:
        #print(row)


# In[155]:


df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv')


# In[156]:


key = df[['Названия строк', 'Сумма по полю Дней с новой ценой']]


# In[159]:


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":

        bot.send_message(message.from_user.id, 'Название эмодзи  | Emojixpress, млнhttps://realty.yandex.ru/offer/1099801596477075200/|5')
        bot.send_message(message.from_user.id, 'https://realty.yandex.ru/offer/1099801596477075200/|10')

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, tte)


# In[160]:


bot.remove_webhook()


# In[161]:


bot.polling(none_stop=True, interval=0)


# In[162]:


data = [
    ['https://realty.yandex.ru/offer/1099801596477075200/',  5],
    ['https://realty.yandex.ru/offer/1333946987119880192/',  8],
    ['https://realty.yandex.ru/offer/1478742844538331904/',  3]]


print('|Ссылка на оффер                                    |Сумма Дней с новой ценой|')
print('-----------------------------------------------------------------------------')
for row in data:
    print('|{: <16}| {: >12.2f}           |'.format(row[0], row[1]))


# In[ ]:




