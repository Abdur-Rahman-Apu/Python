#for converting any dimensional array into one dimensional array
#new_array=old_array.flatten()

from numpy import *
a=array([[1,2,3],[4,5,6]])
print(a)

print("\nConverting into one dimensional array:")
b=a.flatten()
print(b)