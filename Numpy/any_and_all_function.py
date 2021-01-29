'''
any(array_name) this function will return true if any one element is true , empty will print false.
'''

from numpy import *
a=zeros(shape=(3,3),dtype=int)
b=zeros(shape=(3,3),dtype=int)
c=a==b
print(c)

print("Any function:")
new_array=any(c)
print(new_array)

print("\nAll function:")
new_array2=all(c)
print(new_array2)

print("\nFor empty array:")
a=array([])
print(f"Any function={any(a)} and all function={all(a)}")