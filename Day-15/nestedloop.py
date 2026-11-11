"""for row in range(3):
    for col in range(5):
        print(col,end=' ')
    print()"""

#basic pattern
"""for row in range(3):
    for col in range(5):
        print("*",end=' ')
    print()"""

#print 1010

"""for row in range(5):
    for col in range(5):
        if (row+col)%2==0:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
---------------------or----------------------------------"""
"""for row in range(3):
    for col in range(5):
        print(int((row+col)%2==0),end=' ')
    print()"""

"""for row in range(3):
    for col in range(5):
        print(col%2,end=' ')
    print()"""


"""c=1
for row in range(5):
    for col in range(5):
        print(c,end=' ')
        c+=1
        
    print()"""



"""for row in range(5):
    for col in range(5):
        print(row*col,end=' ')
    print()"""



"""for row in range(5):
    for col in range(row+1):
        print("*",end=' ')
    print()"""
n=int(input())
for row in range(n):
    for col in range(n-row):
        print("*",end=' ')
    print()