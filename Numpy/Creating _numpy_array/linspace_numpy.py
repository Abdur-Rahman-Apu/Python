'''
array_name=linspace(start,stop,num=int,dtype=,axis=0,retstep=False,endpoint=True)

'''

from numpy import *
a=linspace(1,5,num=10,axis=0)
print(a)

#access element
print("Access element:")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print("Array length is=",len(a))
print()
#access array using for loop
for i in range(len(a)):
    print(f"Index {i}={a[i]}")
