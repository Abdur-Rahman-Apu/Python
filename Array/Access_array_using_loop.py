from array import *
a=array('f',[1,2,3,4,5])

print("Without index:")
for element in a:
    print(element)

print("With index:")
for index in range(len(a)):
    print(f"a[{index}]={a[index]}")