#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# Write a Python Function for finding a given number is prime or not and do unit testing on it using PyLint and Unittest Library

# In[1]:


get_ipython().system(' pip install pylint')


# In[2]:


get_ipython().system(' pip install unittest2')


# In[12]:


get_ipython().run_cell_magic('writefile', 'primefile.py', "'''\nThis file returns true if number is prime else its returns false\n'''\n\ndef isprimeornot(num):\n    '''\n    Functions return whether the number is prime or not.\n    '''\n    if num > 1:\n        for item in range(2, num):\n            if num%item == 0:\n                return str(num)+' is not prime'\n        else:\n            return str(num)+' is prime'\n\nNUM = int(input('Enter the number - '))\nSTRING = isprimeornot(NUM)\nprint(STRING)")


# In[13]:


get_ipython().system(' pylint "primefile.py"')


# In[1]:


import primefile


# In[6]:


get_ipython().run_cell_magic('writefile', 'testprime.py', '\nimport primefile\nimport unittest2\n\nclass testprime(unittest2.TestCase):\n    def testnumber(self):\n        num = 6\n        result = primefile.isprimeornot(num)\n        self.assertEqual(result,\'6 is not prime\')\n        \nif __name__ == "__main__":\n    unittest2.main()')


# In[1]:


import testprime


# In[ ]:


get_ipython().system(' python testprime.py')


# # Assignment-2
# Make a generator program for returning armstrong numbers in between 1-1000 in a generator object

# In[47]:


def armstrongnumber(num):
    for item in num:
        order=len(str(item))
        temp=item
        summ=0
        while temp>0:
            digit=temp%10
            summ+=digit**order
            temp=temp//10
        if item==summ:
            yield item


# In[48]:


lst=list(range(1,1001))


# In[50]:


print(list(armstrongnumber(lst)))


# In[ ]:




