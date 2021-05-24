#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r
import csv
import io
import urllib.request


# In[70]:


import telebot


# In[71]:


bot = telebot.TeleBot('1884501099:AAGG33pv_ZkikRHYGDHYXMX9qps-qgUIe7o')


# In[82]:


#@bot.message_handler(commands=['start'])
#def send_welcome(message):
    #bot.reply_to(message, f'Привет! Я бот, которые будет помогать сервису стать лучше')


# In[83]:


df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv')


# In[84]:


key = df[['Названия строк', 'Сумма по полю Дней с новой ценой']]


# In[85]:


df = key[key['Сумма по полю Дней с новой ценой'] >= 10].reset_index()
df = df.drop(['index'], axis = 1)


# In[86]:


df


# In[88]:


@bot.message_handler(content_types=['document'])
def get_text_messages(message):
        bot.send_message(message.from_user.id, 'https://realty.yandex.ru/offer/1099801596477075200/|5')
        bot.send_message(message.from_user.id, 'https://realty.yandex.ru/offer/1099801596477075200/|10')
        bot.send_message(message.from_user.id, 'https://realty.yandex.ru/offer/1099801596477075200/|10')


# In[89]:


bot.remove_webhook()


# In[54]:


#!pip install schedule


# from datetime import datetime
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

# if current_time=='18:19:00':
#     def test_send_message():
#             ret_msg = bot.send_message(-1001217016361, 'Оно работает')
#             assert ret_msg.message_id

# import schedule
# import time
# 
# #def job():
#     #print("I'm working...")
# def send_message():
#     bot.send_message(370921204, 'Hello')
# 
# schedule.every().day.at("17:50").do(send_message)
# 
# 
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# In[161]:


bot.polling(none_stop=True, interval=0)


# data = [
#     ['https://realty.yandex.ru/offer/1099801596477075200/',  5],
#     ['https://realty.yandex.ru/offer/1333946987119880192/',  8],
#     ['https://realty.yandex.ru/offer/1478742844538331904/',  3]]
# 
# 
# print('|Ссылка на оффер                                    |Сумма Дней с новой ценой|')
# print('-----------------------------------------------------------------------------')
# for row in data:
#     print('|{: <16}| {: >12.2f}           |'.format(row[0], row[1]))
# 

# In[ ]:




