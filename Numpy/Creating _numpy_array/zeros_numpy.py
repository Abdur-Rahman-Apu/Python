'''
array_name=zeros(shape,dtype,order='C')
'''
from numpy import *
a=zeros(shape=(3,2),dtype=int,order="C")
print(a)
print("Access element:")
print(a[0][0])

print("\nUsing for loop:")
for r in a:
    for c in r:
        print(c)

print("\nUsing while loop with index:")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(f"Index {i}{j}={a[i][j]}",end=' ')
        j+=1
    print()
    i+=1