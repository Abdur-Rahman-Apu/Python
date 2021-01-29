'''
Numpy is a third party package in python for creating n-dimensional array.
'''

from numpy import *
'''
Create numpy using array function
'''

a=array([1,2,3])
print(a)
print(f"Array a length is {len(a)}")
#access value
print(a[0])
print(a[1])
print(a[2])

#print value using for loop

print("\n Using for loop accesing values:")
for element in a:
    print(element)

#print values using for loop with index

print("\n Using for loop accessing values with index no:")
for i in range(len(a)):
    print(f"index {i}={a[i]}")


