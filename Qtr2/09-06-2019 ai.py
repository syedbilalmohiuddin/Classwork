#!/usr/bin/env python
# coding: utf-8

# In[2]:


lst=[[1,2,3],[4,5,6],[7,8,9]]
#print(lst[1][2])
for i in lst:
    #print(i)
    i.insert(1,10)
    print(i)


# In[3]:


# String Casing
b='Pakistan'
print(b.lower())
print(b.upper())
print(b.title())
print(b.capitalize())
# swapcase make reverse casing
print(b.swapcase())


# In[4]:


#Dictionary
std = {
    'Name': 'abc',
    'Father Name': 'def',
    'Age': '16',
    8:9,
    'Cell No':[12345,6789],
    'Dictionary': {
        'Mobile No': 23156,
        'Land Line': 24568
    }
}
#print(std)
'''
std['Name']='ab'
print(std['Name'])
print(std.keys())
print(std.items())

del std['Name']
for k,v in std.items():
    print(k,v)
'''
#print(std.pop('Name'))
#for st in std:
    #print(st,std[st])
print(std['Cell No'][1])
print(std['Dictionary']['Land Line'])


# In[10]:


std=[]
print('')   

def mainmethod(g):
    print('For Add Student Press 1')
    print('For See Student Press 2')
    print('For Main Menu Press 3')
    
    d=input('Enter Option')
    if d=='1':
        stdinsert(1)
    elif d=='2':
        printstd()
    elif d=='3':
        mainmethod(3)
        
        
def requiredArg (name,age,clas):
    dictio={'Name':name,'Age':age,'Class':clas}
    std.append(dictio)


def stdinsert(h):
    a=input('Enter Student Name')
    b=input('Enter Student Age')
    c=input('Enter Student Class')
    requiredArg(a,b,c)
    print('New Student Add Success fully')
    mainmethod(1)
        

def printstd():
    print(std)
    
mainmethod(1)
        
        



# In[ ]:




