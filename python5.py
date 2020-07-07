#!/usr/bin/env python
# coding: utf-8

# In[21]:


mytuple=("Puja","Aryal",22)
list=[]

list.append(mytuple)
friend_tuple1=("Sabitra","Dhital",22)
friend_tuple2=("Binita","Dulal",22)
friend_tuple3=("Richa","Khadka",22)

list.append(friend_tuple1)
list.append(friend_tuple2)
list.append(friend_tuple3)

print(f'The list of student is :{list}')

list.sort(key=lambda x: x[0])
print(f'the sorted list of student is:{list}')



# In[ ]:




