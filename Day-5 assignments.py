#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# Write a program to identify the sub list [1,1,5] is there in the given list in the same order, if yes print its a  match else
# print it's gone in function.

# In[23]:


lst=[1,1,5]
def sublist(lis):
    a=0
    count=0
    for item in lst:
        for i in range(a,len(lis)):
            if item==lis[i]:
                a=i+1
                count+=1
                break
    if count==len(lst):
        print('its a match')
    else:
        print('its gone')    


# In[50]:


listy=[[1,5,6,5,1,2,3,5],[1,2,3,5,1,2,3,4,6],[1,2,3,4,5,6,7,1,2,3,4,5,5,6,7]]
for lists in listy:
    sublist(lists)


# # Assignment 2
# Make a function for Prime Numbers and use filter to filter out all the prime numbers from 1-2500

# In[38]:


def Prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
    else:
        return str(num)+' neither prime nor composite'


# In[40]:


a=1
b=2500
new_list=filter(Prime,range(a,b))


# In[43]:


print(list(new_list))


# # Assignment 3
# make a lambda function for capitalizing the whole sentence passed using arguments and map all the sentences in the list, with the lambda function.

# In[61]:


a='this is tarun'
b=' '
lst=a.split()
listy=[]
for item in lst:
    listy.append(item.capitalize())
b.join(listy)    


# In[76]:


capitalizestring= lambda v:" ".join(map(lambda x:x.capitalize(),input().split()))


# In[80]:


sent=map(capitalizestring,range(int(input('Enter the number of sentences you wanna enter:'))))
s=list(sent)
print(s)


# In[ ]:




