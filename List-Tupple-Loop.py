#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=5
b=2
a+b


# In[4]:


a=float(input("Enter Temprature"))
if a>=40:
    print("Temprature is high")
elif a>=30     and a<40:
    print("Temprature is normal")
else :
    print("Temprature is high")
    


# In[1]:


ar_1=[2,4,5,6,"ab","cd","ef","gh","ij"]
print(ar_1)
# ar_1.pop()  remove last index
# ar_1.pop(0) remove index of array
# ar_1.append add new item on last
# ar_1.remove(1) find value and remove it on array
"""
comment
Array
ar_1.pop()  remove last index
ar_1.pop(0) remove index of array
ar_1.append add new item on last
ar_1.remove(1) find value and remove it on array
ar_1[3]=8  Replace Value on Given Index
ar_1.insert(2,4) Insert Value on Given Index
ar_2=ar_1[2:4] give value from 2nd index t 4th index
ar_3=ar_1[::4] give value from 2nd index t 4th index
del ar_1(0) 
"""

ar_2=ar_1[2:4] 
ar_3=ar_1[::2] 
ar_4=ar_1[::-1]
ar_1.append(25)
print(ar_1)
print(ar_2)
print(ar_3)
print(ar_4)




# In[26]:


"""
Tupple
its value can not changible
"""
tup =(2,6,8,12,13,15,16)
print(tup)
print(tup[4])
# temp=list(tup) make list from tupple
# temp=tupple(ar_1) make tupple from list


# In[34]:


"""
Loop
"""
for ii in range(1, 6):

    print("*",sep=" ")


# In[ ]:




