#!/usr/bin/env python
# coding: utf-8

# # lists and its default functions

# In[1]:


lst=['Tarun','kalva',[12,32,45],(77,84),12,22.5]


# In[4]:


lst.count(12) #tells the count of element in a list


# In[5]:


lst.reverse() #reverses the list


# In[6]:


lst


# In[7]:


lst


# In[12]:


lst.clear() #clears the list


# In[13]:


lst


# In[15]:


lst.append(22) #adds new element to the list


# In[16]:


lst


# In[22]:


lst.index(22) #returns the index value of element in list


# # Dictionaries and its default functions

# In[23]:


tourism={'hyderabad':'golconda','agra':'tajmahal','mysore':'mysore palace','delhi':'red fort','tamil nadu':'politics'}


# In[40]:


sets=tourism.copy() #copies entire dictionary to sets


# In[28]:


sets


# In[37]:


tourism.get('hyderabad') #gets the value of key provided


# In[31]:


tourism.items() #returns the items in the form of list with key value pairs as tuples


# In[32]:


tourism.values() #returns the values in dictionary


# In[38]:


new_place={'tandur':'stone','vikarabad':'railway junction'}
tourism.update(new_place) #updates the existing dictionary with the new dictionary


# In[39]:


tourism


# # sets and its default functions

# In[55]:


things={1,2,3,4,4,5,5,5,6,6,6,7}


# In[42]:


things #set prints only unique values and deletes the duplicate values from set


# In[43]:


things.add('hello') #adds the argument to the set


# In[44]:


things


# In[61]:


string={'hello',1}
things.difference(string) #returns the difference but doesn't change the original set


# In[60]:


things


# In[62]:


things


# In[63]:


things.difference_update(string) #the set gets updated with the difference of two sets


# In[64]:


things


# In[70]:


integers={3,4,5,10}
things.intersection(integers) #shows the common elements in two sets but doesn't change the original set i.e., things


# In[71]:


things


# In[72]:


things.union(string) #returns the union of two sets


# In[75]:


things.symmetric_difference(integers) #returns the elements which are not present in both sets 


# # Tuples and its default functions

# In[77]:


number=(1,2,3,4,5,(1,2,3))


# In[79]:


number.count(4) #returns the count of element in the tuple


# In[81]:


number.index((1,2,3)) #returns the index of the element in tuple


# # strings and its default functions

# In[148]:


name='taRuN kaLva22'


# In[149]:


name.capitalize() #returns the string with the first letter as capital and remaining all as small


# In[150]:


name.casefold() #converts the string to lowercase


# In[151]:


name.encode() #encodes the string to default UTF-8


# In[157]:


name.split(" ") #splits based on de-limiter


# In[164]:


name.zfill(15) #fills the string with zeroes to match the length in zfill


# In[167]:


name.upper() #converts the string to upper case


# In[ ]:




