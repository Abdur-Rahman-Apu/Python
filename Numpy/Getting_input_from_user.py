from numpy import *
r=int(input("Enter number of rows="))
c=int(input("Enter number of columns="))
a=zeros(shape=(r,c),dtype=int)
print("Zeros function:")
print(a)

print("\nAfter getting element from user:")
for i in range(r):
    for j in range(c):
        a[i][j]=int(input(f"Enter at row={i} and column={j} ="))

print("\nNew array:")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(f"Index {i}{j}={a[i][j]}",end=' ')
        j+=1
    print()
    i+=1

