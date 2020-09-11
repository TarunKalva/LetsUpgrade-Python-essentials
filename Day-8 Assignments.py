#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# Write the decorator function to take input for any kind of function you want to build.
# Here the functions build using Decorators are fibonacci and addition.

# In[4]:


def inputfunction(functionality_function):
    def wrap_function():
        a=int(input('Enter the first number-'))
        b=int(input('Enter the second number-'))
        functionality_function(a,b)
    return wrap_function    


# In[9]:


@inputfunction
def fibonacci(a,b):
    count=0
    nterms=int(input('Enter the range of fibonocci series-'))
    if nterms<=0:
        print('Enter the positive number')
    elif nterms==1:
        print('Fibonocci series is')
        print(a)
    else:
        print('Fibonocci series is')
        while count<=nterms:
            print(a,end=' ')
            f=a+b
            a=b
            b=f
            count+=1


# In[10]:


fibonacci()


# In[11]:


@inputfunction
def addition(a,b):
    print('addition is-',a+b)


# In[12]:


addition()


# # Assignment 2
# Develop a python program to open a file in read only mode and handle exception using error handling.

# In[25]:


fhand=open('test.txt','w')
fhand.write(input())
fhand.close()


# In[26]:


fread=open('test.txt','r')
readfile=fread.read()
print(readfile)
fread.close()


# In[27]:


try:
    writefile=fread.write(input())
    print(writefile)
except:
    print('file cannot be written since it is open in read mode')


# In[ ]:




