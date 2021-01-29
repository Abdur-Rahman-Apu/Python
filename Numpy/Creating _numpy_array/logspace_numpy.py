'''
array_name=logspace(start,stop,dtype=None,endpoint=True,base=10,axis=0)
'''

from numpy import *
a=logspace(1,5,num=5,base=10)
print(a)

#access element
print(a[0],a[1],a[2],a[3],a[4])

#for loop
for i in range(len(a)):
    print(f"Index{i}={a[i]}")