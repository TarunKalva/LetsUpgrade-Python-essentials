#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# print the first armstrong number in the range of 1042000 to 702648265 and exit the loop as soon you encounter
# the first armstrong number. Use while loop

# In[4]:


a = 1042000
b = 702648265
for i in range(a,b+1):
    temp = i
    summ = 0
    order = len(str(i))
    while temp>0:
        digit = temp%10
        summ += digit**order
        temp = temp//10
    if i == summ:
        print('The first armstrong number is - ',i)
        break


# In[ ]:




