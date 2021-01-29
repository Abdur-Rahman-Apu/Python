'''
array_name=where(condition,exp1,exp2)
'''
from array import *
a=array('i',[1,2,3,4])
print(a)
print("\nFirst element of array a:")
print(a[0])

b=array('i',[100,200,300,400])
print("Second element of array b=",b[1])

from numpy import *
d=array([1,2,3,4])
e=array([500,600,700,800])
print("\nArray module and where function:")
f=where(a<b,b,a)
print(f)

print("\nNumpy module and where functon:")
g=where(d<e,e,d)
print(g)