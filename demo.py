# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:00:29 2018

@author: Administrator
"""
import cv2
import numpy as np
a=cv2.imread('0.jpg')
o=a.copy()

b=a[:,:,0]
g=a[:,:,1]
r=a[:,:,2]

I=(b+g+r)/3 

I_inverted=255-I

M = cv2.blur(I_inverted,(15,15)); #均值滤波

h,w=a.shape[:2]

r_new=np.zeros([h,w])
g_new=np.zeros([h,w])
b_new=np.zeros([h,w])
for i in range(h):
    for j in range(w):
        pr,pg,pb=r[i,j],g[i,j],b[i,j]
        q=M[i,j]
        r_new[i,j]=255*(pr/255)**(2**((128-q)/128))
        g_new[i,j]=255*(pg/255)**(2**((128-q)/128))
        b_new[i,j]=255*(pb/255)**(2**((128-q)/128))
        
o[:,:,0],o[:,:,1],o[:,:,2]=b_new,g_new,r_new

cv2.imshow('0',a)
cv2.imshow('out',o)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('out.jpg',o)

