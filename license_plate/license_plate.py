#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageChops
import requests
from io import BytesIO
import re 
import imagehash
import time


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


# In[9]:


original_crop


# In[10]:


response2 = requests.get('http://00.img.avito.st/640x480/11335020100.jpg')
test_image = Image.open(BytesIO(response2.content))


# In[11]:


test_image_crop = test_image.crop((0, 0, 180, 180))


# In[12]:


test_image_crop


# In[13]:


hash_original = imagehash.average_hash(original_crop, hash_size=8)
hash_test = imagehash.average_hash(test_image_crop, hash_size=8)
print(hash_original - hash_test)


# In[14]:


print(hash_original)


# In[15]:


key = ()
for i in links:
    try:
        response3 = requests.get(i)
        test2 = Image.open(BytesIO(response3.content))
        test_image_crop2 = test2.crop((0, 0, 180, 180))
        hash_test2 = imagehash.average_hash(test_image_crop2, hash_size=8)
        different = hash_original - hash_test2
        if different <= 1:
            print('Ссылка с номером:', i)
            break
        else:
            е = 1
            #print(different, i)
    except:
        pass
    #time.sleep(1)


# In[ ]:





# In[ ]:




