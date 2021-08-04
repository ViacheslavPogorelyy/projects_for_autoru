#!/usr/bin/env python
# coding: utf-8

# In[55]:


from PIL import Image
import requests
from io import BytesIO


# In[56]:


offer = 'https://16.img.avito.st/640x480/11335020316.jpg'


# In[107]:


response = requests.get(offer)
original = Image.open(BytesIO(response.content))


# In[108]:


original


# In[87]:


num = re.findall(r'\d{11}', offer)


# In[90]:


for el in num:
    el = int(el)


# In[105]:


links = []

for i in range(0, 350):
    num -= 1
    lin ='https://01.img.avito.st/640x480/{}.jpg'.format(num)
    links.append(lin)


# In[109]:


response = requests.get(offer)
original = Image.open(BytesIO(response.content))


# In[51]:


response = requests.get('http://00.img.avito.st/640x480/11335020100.jpg')
original2 = Image.open(BytesIO(response.content))


# In[110]:


result=ImageChops.difference(original, original2)
result.show()


# In[111]:


result


# In[ ]:




