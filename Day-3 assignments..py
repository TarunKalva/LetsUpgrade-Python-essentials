#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
#  Altitude required is 1000ft and if the input is less than or equal to 1000 send a message as 'safe to land' if the altitude is 
#  in between 1000ft and 5000ft send 'bring down to 1000ft'. If altitude is greater than 5000ft send 'go around and try later'.
#  

# In[1]:


alt=input('Enter the altitude in ft\n')
try:
    altitude=int(alt)
except:
    print('Enter the number')
    quit()
if altitude<=1000:
    print('safe to land')
elif altitude>1000 and altitude<=5000:
    print('Bring the plane down to 1000ft')
else:
    print('go around and try later')


# # Assignment 2
# Using the for loop please print all the prime numbers between 1 to 200 using for loop and range function

# In[17]:


print('1 is neither prime nor composite')
for i in range(1,201):                          #here number is selected.
    if i>1:                                         
        for j in range(2,i):                    #range of numbers from 2 to selected number.
            if (i%j)==0:                        #if number is perfectly devisible then break.
                break
        else:
            print(i,end=',')                    #else print prime number.


# In[ ]:




