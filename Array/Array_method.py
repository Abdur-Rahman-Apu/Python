from array import *
a=array('i',[1,2,3,4,5,6,7,8,9])

#insert element in a place

a.insert(1,10)
print(a)

#fing index of a element

index_of_first=a.index(1)
print(index_of_first)

#add element in array
a.append(10)
print(a)

b=array('i',[1,2,3,4,5,6,7])
a.extend(b)
print(a)
c=array('i',[1,2,3])
a=a+c
print(a)

#size of the array
print(len(a))

#reverse method

a.reverse()
print(a)

#pop method
pop_element=a.pop(1)
print(pop_element)
print(a)

#remove method
a.remove(10)
print(a)