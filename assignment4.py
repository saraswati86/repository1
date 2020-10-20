# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:19:15 2020

@author: Saraswati
"""
'''
r=int(input())
c=int(input())
i=1
k=0
for i in range(i,r+1):
  
  for j in range(c):
    print(i+j+k,end=" ")
  k=k+c-1
  print()


r=int(input())
c=int(input())
'''
'''
r1=list(input())
for i in range(3):
    if(i==0):
        r=int(r1[i])
    if(i==2):
        c=int(r1[2])
        
i=1
k=0
for i in range(i,r+1):
  
  for j in range(c):
    if(j==c-1):
      print(i+j+k)
    else:
      print(i+j+k,end=" ")
          
  k=k+c-1
  print() '''
  
'''  
import random
no_of_element=int(input('enter number of element'))
list_1=[]
sorted_list=[]
sored='false'
for n in range(no_of_element):
    x=(input('enter elements'))
    list_1.append(x)
for n in range(no_of_element):
      print(list_1[n])
      
'''
  
import random
no_of_element=int(input())
list_1=[]
sorted_list=[]
sorted='false'
def swap(l1,a,b):
    y=l1[b]
    x=l1[a]    
    l1[a]=y
    l1[b]=x
    return(l1)
for n in range(no_of_element):
    x=int(input())
    list_1.append(x)
print('sorted list is:')
for n in range(no_of_element):
            sorted_list.append(list_1[n])
            sorted_list.sort()
for n in range(no_of_element):
            print(sorted_list[n])
print('given list is:')
for n in range(no_of_element):
            print(list_1[n])
while(sorted=='false'):
    i=random.randint(0,no_of_element-1)
    j=random.randint(0,no_of_element-1)
    list_1=swap(list_1,i,j)
    count=0
    for n in range(no_of_element):
        if(list_1[n]==sorted_list[n]):
            count=count+1
    if(count==no_of_element):
        sorted='true'
    else:
        sorted='false'
        #continue
    print('after random sort, the current list_1 is :')
    for n in range(no_of_element):
        print(list_1[n])
        
    

  
  

