#array slicing

from array import *
a=array('i',[1,2,3,4,5,6,7,8,9])

print(a[1])
a[1]=10

print(a[1])
b=a[:5]
print(b)
b=a[-1::-1]
print(b)