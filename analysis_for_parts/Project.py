#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time


# In[2]:


shop_1 = pd.read_excel('18602214_clicks.xlsx')
shop_2 = pd.read_excel('19074357_clicks.xlsx')
shop_3 = pd.read_excel('21223632_clicks.xlsx')
shop_4 = pd.read_excel('38025008_clicks.xlsx')
shop_5 = pd.read_excel('42078647_clicks.xlsx')
shop_6 = pd.read_excel('57656624_clicks.xlsx')


# In[3]:


calls_1 = pd.read_excel('Calls_18602214.xlsx')
calls_2 = pd.read_excel('Calls_19074357.xlsx')
calls_3 = pd.read_excel('Calls_21223632.xlsx')
calls_4 = pd.read_excel('Calls_38025008.xlsx')
calls_5 = pd.read_excel('Calls_42078647.xlsx')
calls_6 = pd.read_excel('Calls_57656624.xlsx')


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
# 
# Поскольку пропусков в данных у нас нет, судя по предыдущему пункту, то сразу объединить таблицы для дальнейшейно удобства. Плюс зададим каждой таблице ID.

# In[10]:


col = 1
for i in [shop_1, shop_2, shop_3, shop_4, shop_5, shop_6]:
    i['id'] = 'id_00{}'.format(col)
    col += 1
        
shops = pd.concat([shop_1, shop_2, shop_3, shop_4, shop_5, shop_6],axis = 0)


# Удалим столбец с персональными данными и сразу для удобства переименуем оставшиеся.

# In[11]:


shops = shops.drop(['Ссылка на объявление'], axis= True)

shops.columns = ['time', 'category', 'price', 'count', 'id']


# Теперь переведем дату в соответствующий формат.

# In[12]:


shops['time'] =pd.to_datetime(shops['time'], format='%d.%m.%Y %H:%M:%S', dayfirst=False)

shops


# Теперь тоже самое можно сделать и с другой таблицей по звонкам.

# In[13]:


col = 1
for i in [calls_1, calls_2, calls_3, calls_4, calls_5, calls_6]:
    i['id'] = 'id_00{}'.format(col)
    col += 1
        
calls = pd.concat([calls_1, calls_2, calls_3, calls_4, calls_5, calls_6],axis = 0)


# Вновь удалим лишние столбцы с персональными данными.

# In[14]:


calls = calls.drop(['source', 'proxy', 'target'], axis= True)
calls.columns = ['time', 'result', 'talk_time', 'id']


# In[15]:


calls['time'] =pd.to_datetime(calls['time'], format='%Y-%m-%dT%H:%M:%S', dayfirst=False)
#calls['time'].dt.round('30min')


# In[16]:


calls


# ### Вывод:
# Мы подготовили данные и теперь можно приступать к анализу.

# ## Исследовательский анализ данных
# 
# Поскольку кликов может быть много в короткий промежуток времени, то для удобства сделаем получасовые когорты для постраения графиков.

# In[17]:


shops['hour'] = shops['time'].dt.round('2H')
shops['day'] = shops['time'].dt.round(freq = 'D')


# In[18]:


shops.sample(20)


# Возьмем в качестве примера один из дней и построим график по нему.

# In[19]:


day = shops.query('day == "2021-09-14"')


# In[20]:


day.pivot_table(index='hour', columns='id', values = 'count', aggfunc = 'sum').plot(title='Поведение рекламы в течение дня', figsize = (16,8)).set(xlabel="Время публикации", ylabel="Количество кликов")


# In[ ]:





# In[ ]:




