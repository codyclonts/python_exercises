#!/usr/bin/env python
# coding: utf-8

# In[251]:


#teacher solution

def is_two(x):
    return x==2 or x == '2'


# In[2]:


#1

def is_two(x):
    if ((x== 2) or (x == '2')):
        print(True)
    else:
        print(False)


# In[249]:




# In[284]:


def is_vowel(x):
    if x.lower() in ['a' or 'e' or 'i' or 'o' or 'u']:
        return True
    else:
        return False


# In[291]:





# In[287]:


#2
def is_consonant(x):
    if x.lower() in ['a' or 'e' or 'i' or 'o' or 'u']:
        print(False)
    else:
        print(True)


# In[296]:


#teacher solution 2
def is_consonant(x):
    if type(x) == str:
        only_letters = x.isalpha()
        return only_letters and not is_vowel(x)
    return False


# In[302]:


# is_consonant('cat')


# In[312]:


#Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word if the word starts with a consonant.

def captitalize_consonant(x):
    if type(x) != str:
        return False
    if x[0].lower() not in 'aeiou':
        return(x.capitalize())


# In[317]:


# captitalize_consonant('cats are fast')


# In[ ]:


#5
#Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip():
    bill= input('How much was the bill? ')
    x = float(bill)
    tip =input('What percentage would you like to tip? ')     
    y = (float(tip)/100)* x 
    print('Your total is $', x + y) 


# In[320]:


# calculate_tip()


# In[322]:


#6
#Define a function named apply_discount. 
#It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount():
    total= input('What was the total? ')
    x= float(total)
    discount= input('Discount percentage to be applied ')
    y = (float(discount)/100)* x 
    print('Your final total is $', x-y)


# In[323]:


# apply_discount()


# In[324]:


#7
#Define a function named handle_commas. 
#It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(num):
    num= num.replace(",","")
    return int(num)
    


# In[325]:


# handle_commas('10,000,000')


# In[326]:


#8
#Define a function named get_letter_grade. 
#It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade():
    grade = int(input('What was your grade from 0-100? '))
    if grade >= 90 and grade <= 100:
        print( "A:", grade)
        
    elif grade >= 80 and grade <=89:
        print ("B:", grade)
        
    elif grade >= 70 and grade <=79:
        print ("C:", grade)
       
    elif grade >= 60 and grade <=69:
        print ("D:", grade)
        
    elif grade < 60:
        print ("F:", grade)


# In[327]:


# get_letter_grade()


# In[328]:


#9 
#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def no_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in word:
        if x.lower() in vowels:
            word = word.replace (x,"")
    return(word)


# In[329]:


# no_vowels('abracadabra')


# In[335]:


#10
#Define a function named normalize_name. 
#It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed

def normalize_name(string):
    output = ''
    for x in string:
        if x.isidentifier() or x == ' ':
            output += x
        string = string.strip()
        string = string.lower()
        string = string.replace(" ", "_")
    return(string)

    


# In[337]:


# normalize_name(' First and Last name 32 @')


# In[ ]:




