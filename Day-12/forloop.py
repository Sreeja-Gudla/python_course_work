#str lsit tuple set dic range()

#for i in seq:
    #stmt

#string
"""s='codegnan'
for i in s:
    print(i)"""


"""a=input("Enter a string: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i)"""


#list
"""s=[12,23,34,56,23,44]
for i in s:
    print(i)


a=list(map(int,input("Enter the nums: ").split()))
for i in a:
    if i%2==0:
        print(i)"""


#tuple
"""s=(12,23,34,56,23,44)
for i in s:
    print(i)

sumoftuple=0
a=tuple(map(int,input("Enter the nums: ").split()))
for i in a:
    sumoftuple+=i
print("Sum of tuple is ",sumoftuple)"""


#set
"""s={12,23,34,56,23,44}
for i in s:
    print(i)

max=0
a=set(map(int,input("Enter the nums: ").split()))
for i in a:
    if i>max:
        max=i
print("Max of set: ",max)"""


#dictionary
"""marks={'python':20,'css':25,'html':33,'java':66,'mysql':66}
for i in marks:
    print(i,marks[i])


sum=0
marks={'python':20,'css':25,'html':33,'java':66,'mysql':66}
for i in marks:
    sum+=marks[i]
print("total:",sum)"""



#range
"""for i in range(1,11):
    print(i)


for i in range(20,0,-1):
    print(i)

for i in range(2,101,2):
    print(i,end=" ")"""



# print a table 
"""n=int(input("Enter a num: "))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')"""

"""c='codegnan'
for i in range(len(c)):
    print(c[i],i,end=" ")"""

"""l=[12,34,633,44,75,99,67,22,19]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum+=i
print(sum)
"""


"""l=[12,34,633,44,75,99,67,22,19]
product=1
for i in range(len(l)):
    if l[i]%2!=0:
        product*=i
print(product)
"""
#break 
"""for i in range(1,11):
    if i==5:
        break
    print(i)"""

# continue

"""for i in range(1,11):
    if i==5:
        continue
    print(i)"""

#pass
for i in range(1,10):
    pass


if True:
    pass

class Booking:
    pass

def func():
    pass