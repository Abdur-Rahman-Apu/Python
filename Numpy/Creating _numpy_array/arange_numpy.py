'''

array_name=arrange(start,stop,step,dtype=None)
'''
from numpy import *
a=arange(1,10,2,dtype=float)
print(a)

print(a[0],a[1],a[2])

#access using for loop
print("Using for loop:")

for i in range(len(a)):
    print(f"Index{i}={a[i]}")