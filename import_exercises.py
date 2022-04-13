#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import functions_exercises as funct


# In[ ]:


#funct.is_two(3)


# In[ ]:


#funct.is_vowel('x')


# In[ ]:


#funct.captitalize_consonant('cats are fast')


# In[1]:


from functions_exercises import calculate_tip


# In[2]:


calculate_tip()


# In[3]:


from functions_exercises import get_letter_grade


# In[4]:


get_letter_grade()


# In[15]:


import itertools


# In[25]:


letter = ['A','B','C']
number = [1,2,3]


# In[27]:


len(list(itertools.product(letter, number)))


# In[17]:


letters = ['A', 'B', 'C' ,'D']


# In[18]:


#How many different combinations are there of 2 letters from "abcd"?
len(list(itertools.combinations(letters,2)))


# In[19]:


len(list(itertools.permutations(letters,2)))


# In[ ]:




