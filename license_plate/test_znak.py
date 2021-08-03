#!/usr/bin/env python
# coding: utf-8

# In[80]:


from PIL import Image, ImageChops


# In[81]:


image_1=Image.open('авита.jpg')
image_2=Image.open('авита_номер.jpg')
image_3=Image.open('тачка.jpg')
image_4=Image.open('тачка_сзади.jpg')


# In[82]:


result=ImageChops.difference(image_1, image_2)
result.show()


# In[83]:


result.getbbox()


# In[84]:


print(result.getbbox())

