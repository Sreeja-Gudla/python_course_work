"""l=[1,2,0,7,8,0,0,3,0,0,0,0,4,5]
while 0 in l:
    l.remove(0)
print(l)"""

#to print 1to 10 num using whileloop
"""i=1
while i<11:
    print(i)
    i+=1"""
# print revrse 10to1
"""i=10
while i>0:
    print(i)
    i-=1"""
# print even numbers from 1 to 100
"""i=2
while i<101:
    print(i)
    i+=2
     """
# print multiples of a number
"""i=5
while i<101:
    print(i)
    i+=5"""

#how to iterate a string

"""a='python programming'
i=0
while i<len(a):
    print(i,a[i])
    i+=1"""

#how to iterate a list

"""a=[1,2,3,4,6]
i=0
while i<len(a):
    print(i,a[i])
    i+=1"""

#how to iterate a tuple
"""a=(1,2,3,4,6)
i=0
while i<len(a):
    print(i,a[i])
    i+=1 """

#break and continue
"""a=(1,2,5,4,6)
i=0
while i<len(a):
    if a[i]==5:
        break
    print(i,a[i])
    i+=1"""

"""a=[1,2,5,4,6]
i=0
while i<len(a)-1:
    i+=1
    if a[i]==5:
        continue
    print(i,a[i])
    """


# we have a string pythonprogramming
#output shld be like pg,yn

c='pythonprogramming'
i=0
j=len(c)-1
while i<=j:
    if i==j:
        print(c[i])
    else:
        print(c[i],c[j])
    i+=1
    j-=1