#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
import numpy as np
import requests as r


# In[56]:


text = r.get('https://www.avito.ru/rostov-na-donu/zapchasti_i_aksessuary/toyo_185_65_r14_2sht_2136520396').text
photo = re.findall(r'(https://www.avito.ru/img/share/auto/+\d{11})', text)


# In[63]:


avito_photo = pd.DataFrame(data = photo, columns = ['img'])
avito_photo = avito_photo.drop_duplicates(subset=['img']).reset_index()


# In[64]:


links = []
for i in range(len(avito_photo)):
    result = avito_photo['img'][i].replace('https://www.avito.ru/img/share/auto/', '')
    id_avito = "https://30.img.avito.st/1280x960/{}.jpg".format(result)
    links.append(id_avito)
    
links    

