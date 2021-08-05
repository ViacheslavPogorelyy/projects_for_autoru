#!/usr/bin/env python
# coding: utf-8

# In[378]:


from PIL import Image, ImageChops
import requests
from io import BytesIO
import re 
import imagehash
import time


# In[412]:


offer = 'http://05.img.avito.st/640x480/11336196705.jpg'


# In[413]:


offer_id = re.findall(r'\d{11}', offer)


# In[414]:


for element in offer_id:
    offer_id = int(element)


# In[415]:


links = []

for i in range(0, 300):
    offer_id -= 1
    last_num = str(offer_id)[-2:]
    short_link = 'https://{}.img.avito.st/'.format(last_num)
    all_link = short_link+'640x480/{}.jpg'.format(offer_id)
    links.append(all_link)


# In[416]:


response = requests.get(offer)
original = Image.open(BytesIO(response.content))


# In[417]:


original


# In[418]:


original_crop = original.crop((0, 0, 150, 150))


# In[419]:


original_crop


# In[420]:


response2 = requests.get('https://05.img.avito.st/640x480/11335020005.jpg')
test_image = Image.open(BytesIO(response2.content))


# In[421]:


test_image_crop = test_image.crop((0, 0, 150, 150))


# In[422]:


test_image_crop


# In[423]:


hash_original = imagehash.average_hash(original_crop)
hash_test = imagehash.average_hash(test_image_crop)
print(hash_original - hash_test)


# In[424]:


key = ()
for i in links:
    try:
        response3 = requests.get(i)
        test2 = Image.open(BytesIO(response3.content))
        test_image_crop2 = test2.crop((0, 0, 150, 150))
        hash_test2 = imagehash.average_hash(test_image_crop2)
        different = hash_original - hash_test2
        if different < 1:
            print('Ссылка с номером:', i)
            break
        else:
            е = 1
    except:
        pass
    #time.sleep(1)


# In[ ]:




