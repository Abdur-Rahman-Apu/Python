'''
array_name=ones(shape,dtyp=float,order='C')
'''

from numpy import *
a=ones(shape=(3,3),dtype=int)
print(a)

print("\nAccess element by using for loop:")
for r in a:
    for c in r:
        print(c,end=' ')
    print()

print("\nAccess element with index using while loop:")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(f"Index {i}{j}={a[i][j]}",end=' ')
        j+=1
    print()
    i+=1