#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageChops
import requests
from io import BytesIO
import re 
import imagehash
import time


# Передаем ссылку на изображение с заглушкой номерного знака сюда руками.

# In[2]:


offer = 'https://86.img.avito.st/640x480/11600735986.jpg'


# In[3]:


offer_id = re.findall(r'\d{11}', offer)


# In[4]:


for element in offer_id:
    offer_id = int(element)


# In[5]:


links = []

for i in range(0, 1800):
    offer_id -= 1
    last_num = str(offer_id)[-2:]
    short_link = 'https://{}.img.avito.st/'.format(last_num)
    all_link = short_link+'640x480/{}.jpg'.format(offer_id)
    links.append(all_link)


# In[6]:


response = requests.get(offer)
original = Image.open(BytesIO(response.content))


# In[7]:


original


# In[8]:


original_crop = original.crop((0, 0, 180, 180))
hash_original = imagehash.average_hash(original_crop, hash_size=8)


# In[9]:


for i in links:
    try:
        response_offer = requests.get(i)
        image = Image.open(BytesIO(response_offer.content))
        test_image_crop = image.crop((0, 0, 180, 180))
        hash_image = imagehash.average_hash(test_image_crop, hash_size=8)
        different = hash_original - hash_image
        if different <= 1:
            print('Ссылка с номером:', i)
            break
        else:
            pass
    except:
        pass


# In[ ]:





# In[ ]:




