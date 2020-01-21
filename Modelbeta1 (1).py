#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pygame
import time
import smtplib
from matplotlib import pyplot as plt
from matplotlib import image as mpimg


# In[2]:


def plt_show(image, title=""):
       if len(image.shape) == 3:
           image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
           plt.axis("off")
           plt.title(title)
           plt.imshow(image1, cmap=plt.cm.Greys_r)
           plt.show()


# In[3]:


def img_resize(image, width=None, height=None, inter = cv2.INTER_AREA):
    dim = None
    h = image.shape[0]
    w = image.shape[1]
    chan = image.shape[2]
    if height is None and width is None :
        return image
    if width is None :
        r = height/float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width,int(h * r))
    
    resized = cv2.resize(image, dim, interpolation = inter)
    
    return resized
 
def severity_factor(contours):
    x = len(contours)
    if x>800:
        x=3
    elif x<500:
        x=1
    else:
        x=2
    return x


# In[4]:


r_image1 = mpimg.imread('D:\Downloads\Pothole3.jpg')
r_image2 = img_resize(r_image1, width = 275, height = 180)


# In[5]:


plt_show(r_image2)


# In[6]:


plt.title("Pothole Image")
plt.imshow(r_image2)
plt.show()


# In[7]:


im = r_image2;
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
plt_show(imgray)


# In[8]:


ret, thresh = cv2.threshold(imgray,127,255,0)


# In[9]:


image1, contours1, hierarchy1 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# In[10]:


plt_show(image1)


# In[11]:


img2 = im.copy()
plt.imshow(img2)


# In[12]:


out = cv2.drawContours(img2, contours1, -1, (0,250,0),1)
plt.imshow(out)


# In[13]:



plt.subplot(331),plt.imshow(im),plt.title('GRAY')
plt.xticks([]), plt.yticks([])


# In[14]:


img = mpimg.imread('D:\Downloads\Pothole3.jpg',0)
plt.imshow(img)


# In[15]:


plt.imshow(img2)


# In[16]:


image, contours, hierarchy = cv2.findContours(thresh, 1, 2)
print(severity_factor(contours))


# In[ ]:



for c in contours:
    rect = cv2.boundingRect(c)
    if rect[2] < 100 or rect[3] < 100: continue
    #print cv2.contourArea(c)
    x,y,w,h = rect
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),8)
    cv2.putText(img2,'Moth Detected',(x+w+40,y+h),0,2.0,(0,255,0))
    
    plt.title("Moth Detected Pothole Image")
    plt.imshow(img2)
    plt.show()
    
cv2.imshow("Show",img2)
#cv2.imshow('img' , img_resize)
x = cv2.waitKey(0)
if x == 27:
    cv2.destroyWindow('img')
cv2.waitKey()  
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




