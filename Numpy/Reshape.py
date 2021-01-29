'''
new_array=reshape(array_name,(r,c))

'''

from numpy import *
a=array([1,2,3,4,5,6])
b=reshape(a,(3,2))
c=reshape(a,(6,1))
print(a)
print(b)
print(c)

d=reshape(a,(2,3))
print(d)