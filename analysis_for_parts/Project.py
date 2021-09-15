#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


# ## Знакомство с данными

# In[2]:


shop_1 = pd.read_excel('11124040_clicks.xlsx')
shop_2 = pd.read_excel('2033339_clicks.xlsx')
shop_3 = pd.read_excel('21313454_clicks.xlsx')
shop_4 = pd.read_excel('3275769_clicks.xlsx')
shop_5 = pd.read_excel('55553302_clicks.xlsx')
shop_6 = pd.read_excel('8335728_clicks.xlsx')


# In[3]:


calls_1 = pd.read_excel('Calls_11124040.xlsx')
calls_2 = pd.read_excel('Calls_2033339.xlsx')
calls_3 = pd.read_excel('Calls_21313454.xlsx')
calls_4 = pd.read_excel('Calls_3275769.xlsx')
calls_5 = pd.read_excel('Calls_55553302.xlsx')
calls_6 = pd.read_excel('Calls_8335728.xlsx')


# In[4]:


shop_1.info()


# In[5]:


shop_2.info()


# In[6]:


shop_3.info()


# In[7]:


shop_4.info()


# In[8]:


shop_5.info()


# In[9]:


shop_6.info()


# ### Вывод:
# Мы ознакомились с данными и теперь можем приступить к предобработке.

# ## Предобработка данных

# Поскольку пропусков в данных у нас нет, судя по предыдущему пункту, то сразу можем приступить к переводу колонки `time` к необходимому формату + переименуем столбцы для удобства.

# In[10]:


for i in [shop_1, shop_2, shop_3, shop_4, shop_5, shop_6]:
    i.columns = ['time', 'category', 'link', 'price', 'count']
    i['time'] = pd.to_datetime(i['time'])


# Тоже самое можно сделать с данными по звонкам.

# In[11]:


for i in [calls_1, calls_2, calls_3, calls_4, calls_5, calls_6]:
    i.columns = ['call_time', 'result', 'talk_second', 'source', 'proxy','target']
    i['call_time'] = pd.to_datetime(i['call_time'])

