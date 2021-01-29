'''
view method will make a new array and this and orginal array are dependent
'''
from numpy import *
a=array([1,2,3,4])
b=a.view()
print("Array of a:",a)
print("Array of b:",b)
print("\nView method:")
print("Changing b array index no 1 element with value 6:")
b[1]=6
print("Array of a:",a)
print("Array of b:",b)

print("\nChanging a array index no 1 element with value 2:")
a[1]=2
print("Array of a:",a)
print("Array of b:",b)
