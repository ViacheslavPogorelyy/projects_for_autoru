#!/usr/bin/env python
# coding: utf-8

# In[133]:


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


# In[59]:


import telebot


# In[60]:


bot = telebot.TeleBot('1884501099:AAGG33pv_ZkikRHYGDHYXMX9qps-qgUIe7o')
channel_login = '@for_vertis'
sleep = '10'
#-1001217016361


# In[61]:


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# In[62]:


df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Qqeac9VXzEiB78lRnsQocY0IIibQyfnscqIchX8CMlo/export?format=csv')


# In[63]:


key = df[['Названия строк', 'Сумма по полю Дней с новой ценой']]


# In[64]:


df = key[key['Сумма по полю Дней с новой ценой'] >= 10].reset_index()
df = df.drop(['index'], axis = 1)


# In[149]:


mytable = PrettyTable()


# In[151]:


mytable.field_names = ["Ссылка на оффер", "Сумма с новой ценой"]
# добавление данных по одной строке за раз
for i in range(len(df)):
    mytable.add_row([df['Названия строк'][i], df['Сумма по полю Дней с новой ценой'][i]])
# вывод таблицы в терминал
print(mytable)


# In[152]:


Row_list =[]
for i in range((df.shape[0])):
    Row_list.append(list(df.iloc[i, :]))


# In[ ]:





# In[128]:


for row in Row_list:
    t = ('{:} {: >12}'.format(row[0], row[1]))
    bot.send_message(-1001217016361, t, disable_web_page_preview = True)
    time.sleep(3)


# In[99]:


for row in Row_list:
    t = ('{: <13} {: >10} '.format(row[0], row[1]))
    bot.send_message(-1001217016361, t, disable_web_page_preview = True)


# In[153]:


bot.send_message(-1001217016361, mytable, disable_web_page_preview = True)


# In[9]:


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# In[95]:


bot.remove_webhook()


# In[54]:


#!pip install schedule


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

# In[114]:


bot.polling(none_stop=True, interval=0)


# In[129]:


data = [
    ['https://realty.yandex.ru/offer/1099801596477075200/',  5],
    ['https://realty.yandex.ru/offer/1333946987119880192/',  8],
    ['https://realty.yandex.ru/offer/1478742844538331904/',  3]]


print('|Ссылка на оффер                                    |Сумма Дней с новой ценой|')
print('-----------------------------------------------------------------------------')
for row in Row_list:
    print('|{: <16}| {: >12.2f}           |'.format(row[0], row[1]))


# In[143]:


mytable = PrettyTable()


# In[144]:


mytable.field_names = ["Ссылка на оффер", "Сумма Дней с новой ценой"]
# добавление данных по одной строке за раз
for i in range(len(df)):
    mytable.add_row([df['Названия строк'][i], df['Сумма по полю Дней с новой ценой'][i]])
# вывод таблицы в терминал
print(mytable)


# In[ ]:




