#!/usr/bin/env python
# coding: utf-8

# In[10]:


#dictionary
frut=["Apple","Mango","Banana","Orange","Grapes","Apple","Mango","Banana","Orange","Grapes"]
dict = {}
print("Mango" in frut)

for i in frut:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


# In[16]:


#function
def cal(a,b):
    return a+b
cal(1,2)
cal(b=4,a=3)


# In[35]:




def lstlenth(lst):
    bb=0
    for i in lst:
        bb+=1
    return bb

print(lstlenth([1,3,5,6,8]))
lst11=[1,2,3,5]
print(len(lst11) )  

def lstsum(lst):
    bb=0
    for i in lst:
        bb+=i
    return bb
def lstavg(lst):
    return lstsum(lst)/lstlenth(lst)

#*c gives value in tupple
#** gives value in List
def lstmlt(a,b,*c):
    j=0
    for i in c:
        j+=i       
    return a+b+j

lstvalue =[1,3,5,6,8]

print(lstsum(lstvalue))
print(lstavg(lstvalue))
print(lstmlt(5,6,9,8,7,5,6))




# In[ ]:




