#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# Create a bank account class with attributes ownername and balance and create two methods deposit and withdraw to add and remove money from bank and if the withdraw amount is more than balance return error message.

# In[12]:


class bankaccount:
    def __init__(self,ownerName,balance):
        self.ownerName=ownerName
        self.balance=balance
    def deposit(self,dep):
        self.balance=self.balance+dep
        return 'your account is deposited with '+str(dep)+' and the available balance is '+str(self.balance)
    def withdraw(self,wdr):
        if wdr>self.balance:
            return 'your account doesnt have sufficient balance'
        else:
            self.balance=self.balance-wdr
            return str(wdr)+' is withdrawn and the balance remaining is '+str(self.balance)


# In[13]:


myaccount=bankaccount('Tarun',85000)


# In[14]:


myaccount.deposit(45000)


# In[15]:


myaccount.withdraw(100000)


# In[16]:


myaccount.withdraw(50000)


# In[17]:


myaccount.deposit(50000)


# In[18]:


myaccount.withdraw(65000)


# # Assignment 2
# Create a class cone that has two attributes R-Radius and H-height and two methods Volume-pi**r**r**(h/3) and surface area-base:pi**r**r,side:pi**r**(r**r+h**h)***1/2

# In[36]:


import math
class cone:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def volume(self):
        return math.pi*self.r*self.r*(self.h/3)
    def surface_area(self):
        return math.pi*self.r*(self.r+math.sqrt(self.h**2+self.r**2))


# In[37]:


c=cone(5,6)


# In[38]:


c.volume()


# In[39]:


c.surface_area()


# In[ ]:




