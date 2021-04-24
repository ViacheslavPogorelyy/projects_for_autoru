#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r


# In[97]:


text = r.get('https://www.avito.ru/rostov-na-donu/zapchasti_i_aksessuary/toyo_185_65_r14_2sht_2136520396').text
photo = re.findall(r'(https://www.avito.ru/img/share/auto/+\d{11})', text)
avito_photo = pd.DataFrame(data = photo, columns = ['img'])
avito_photo = avito_photo.drop_duplicates(subset=['img']).reset_index()


# In[98]:


avito_photo.columns


# In[99]:


avito_photo['img']


# In[ ]:


avito_photo = avito_photo['img'][0].replace('//', 'gg') 


# In[ ]:


avito_photo


# In[ ]:


res_str = avito_photo['img'][:36] +str[4:]


# In[35]:


print("https://30.img.avito.st/640x480/{}.jpg".format(avito_photo['img'])) 


# In[ ]:




