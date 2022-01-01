#!/usr/bin/env python
# coding: utf-8

# In[3]:



### task1

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


# In[6]:


## task 2

import sys
print("Python version we are yousing right now")
print (sys.version)


# In[8]:



## task 3

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[10]:


## task 4

from math import pi

value = float(input ("Input the radius of the circle : "))
calculateArea = str(pi * value**2);
print ("The area of the circle with radius " + str(value) + " is: " + calculateArea)


# In[12]:


## task 5
fname = input("enter  your First Name : ")
lname = input("enter  your Last Name : ")
print (  lname + " " + fname)


# In[14]:


## task 6 

a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("addition is :",a + b)

