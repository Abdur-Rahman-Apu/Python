'''
array_name=nonzero(a) this will return index no of nonzero elements
'''
from numpy import *
a=array([1,0,2,0,3,0])
print("Orginal array:")
print(a)
b=nonzero(a)
print("\nNew array:")
print(b)