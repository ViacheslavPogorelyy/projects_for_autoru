#!/usr/bin/env python
# coding: utf-8

# In[401]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time


# In[402]:


shop_1 = pd.read_excel('11124040_clicks.xlsx')
shop_2 = pd.read_excel('2033339_clicks.xlsx')
shop_3 = pd.read_excel('21313454_clicks.xlsx')
shop_4 = pd.read_excel('3275769_clicks.xlsx')
shop_5 = pd.read_excel('55553302_clicks.xlsx')
shop_6 = pd.read_excel('8335728_clicks.xlsx')


# In[403]:


calls_1 = pd.read_excel('Calls_11124040.xlsx')
calls_2 = pd.read_excel('Calls_2033339.xlsx')
calls_3 = pd.read_excel('Calls_21313454.xlsx')
calls_4 = pd.read_excel('Calls_3275769.xlsx')
calls_5 = pd.read_excel('Calls_55553302.xlsx')
calls_6 = pd.read_excel('Calls_8335728.xlsx')


# In[404]:


shop_1.info()


# In[405]:


shop_2.info()


# In[406]:


shop_3.info()


# In[407]:


shop_4.info()


# In[408]:


shop_5.info()


# In[409]:


shop_6.info()


# ### Вывод:
# Мы ознакомились с данными и теперь можем приступить к предобработке.

# ## Предобработка данных
# 
# Поскольку пропусков в данных у нас нет, судя по предыдущему пункту, то сразу объединить таблицы для дальнейшейно удобства. Плюс зададим каждой таблице ID.

# In[410]:


col = 1
for i in [shop_1, shop_2, shop_3, shop_4, shop_5, shop_6]:
    i['id'] = 'id_00{}'.format(col)
    col += 1
        
shops = pd.concat([shop_1, shop_2, shop_3, shop_4, shop_5, shop_6],axis = 0)

shops


# Переименуем столбцы для удоства.

# In[411]:


shops.columns = ['time', 'category', 'link', 'price', 'count', 'id']


# Тоже самое можно сделать с данными по звонкам.

# In[412]:


shops['time'] =pd.to_datetime(shops['time'], format='%d.%m.%Y %H:%M:%S', dayfirst=False)

shops


# Теперь тоже самое можно сделать и с другой таблицей по звонкам.

# In[413]:


col = 1
for i in [calls_1, calls_2, calls_3, calls_4, calls_5, calls_6]:
    i['id'] = 'id_00{}'.format(col)
    col += 1
        
calls = pd.concat([calls_1, calls_2, calls_3, calls_4, calls_5, calls_6],axis = 0)


# Чтобы не показывать персональные данные, удалим лишние столбцы.

# In[414]:


calls = calls.drop(['source', 'proxy', 'target'], axis= True)
calls.columns = ['time', 'result', 'talk_time', 'id']

calls


# In[426]:


calls['time'] =pd.to_datetime(calls['time'], format='%Y-%m-%dT%H:%M:%S', dayfirst=False)
#calls['time'].dt.round('30min')


# In[427]:


calls


# ### Вывод:
# Мы подготовили данные и теперь можно приступать к анализу.

# ## Исследовательский анализ данных
# 
# Поскольку кликов может быть много в короткий промежуток времени, то для удобства сделаем получасовые когорты для постраения графиков.

# In[428]:


shops['hour'] = shops['time'].dt.round('30min')
shops['day'] = shops['time'].dt.round(freq = 'D')


# In[430]:


shops.sample(20)


# In[435]:


shops.pivot_table(index='hour', columns='id', values = 'count', aggfunc = 'sum').plot(title='Распределение доходов платформ по годам').set(xlabel="Дата публикации", ylabel="Количество кликов")


# In[ ]:



