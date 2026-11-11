"""n=int(input())
for row in range(n):
    for sp in range(n-1-row):
        print(" ",end=' ')
    for col in range(n-row):
        print("*",end=' ')
    print()"""

#output
"""         * 
          * * 
        * * * 
      * * * * 
    * * * * * 
  * * * * * * 
* * * * * * * """
'---------------------------------------------------------------'
"""n=int(input())
for row in range(n):
    for sp in range(row):
        print(" ",end=' ')
    for col in range(n-row):
        print("*",end=' ')
    print()"""
#output
"""* * * * * 
     * * * * 
       * * * 
         * * 
           * """
'----------------------------------------------------------'
"""n=int(input())
mid=n//2
for row in range(n):
    if row<=mid:
        for col in range(row+1):
            print("*",end=' ')
    else:

        for col in range(n-row):
            print("*",end=' ')
    print()
"""
"short method"
"""n=int(input()) 
mid=n//2
for row in range(n):
        print('* '*(row+1) if row<=mid else '* '*(n-row))
"""
"OUTPUT"
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
'----------------------------------------------------------------------'
"""n = int(input()) 
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(' ', end=' ')  
    print()"""
"OUTPUT"
"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
"""
'-----------------------------------------------'

"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i==m or j == 0 or j == n - 1 or j==m:
            print("*", end=" ")
        else:
            print(' ', end=' ')  
    print()"""

"OUTPUT"
"""
* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * *
"""
'------------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j==0 or i==n-1 or j==n-1 or i==m or j==m or i==j or i+j==n-1:
            print("*", end=" ")
        else:
            print(' ', end=' ')  
    print()"""
"OUTPUT"
"""
* * * * * * * * * 
* *     *     * * 
*   *   *   *   * 
*     * * *     * 
* * * * * * * * * 
*     * * *     * 
*   *   *   *   * 
* *     *     * * 
* * * * * * * * * """
'----------------------------------------------'

"""
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j==0 or i==n-1 or (j==n-1 and i>=m) or  (i==m and j>=m):
            print("*", end=" ")
        else:
            print(' ', end=' ')  
    print()
"""
"OUTPUT"
"""
* * * * * * * * * 
*                 
*                 
*                 
*       * * * * * 
*               * 
*               * 
*               * 
* * * * * * * * * 
"""
'---------------------------------------------'
"""
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j==m or (i==n-1 and j<=m) or (j==0 and i>=m):
            print("*", end=" ")
        else:
            print(' ', end=' ')  
    print()
"""
"OUTPUT"
"""
* * * * * * * * * 
        *         
        *         
        *         
*       *         
*       *         
*       *         
*       *         
* * * * *  
"""
'------------------------------------------------------------------'
"""
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print("*", end=" ")
        else:
            print(' ', end=' ')  
    print()
    """
"OUTPUT"
'''
*               * 
* *           * * 
*   *       *   * 
*     *   *     * 
*       *       * 
*               * 
*               * 
*               * 
*               * 
'''
'---------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or j==n-1 or i==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * *
*       *
* * * * *
*       *
*       *
"""
'--------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or j==n-1 or i==m or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
'''
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 
'''
'--------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
'''
* * * * * 
*         
*         
*         
* * * * * 
'''
'----------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
"""
'---------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or i==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
*         
* * * * * 
*         
* * * * * 
"""
'-------------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
*         
* * * * * 
*         
*  
"""
'---------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==m or j==n-1 or i==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
'''
*       * 
*       * 
* * * * * 
*       * 
*       * 
'''
'-----------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
    *     
    *     
    *     
* * * * * 
"""
'---------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
*         
*         
*         
*         
* * * * *
"""
'------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
*       * 
* *     * 
*   *   * 
*     * * 
*       * 
"""
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1 or i==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
"""
'--------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==m or (j==n-1 and i<=m) or i==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
'''
* * * * * 
*       * 
* * * * * 
*         
*  
'''
'----------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==m or(j==0 and i<=m) or (j==n-1 and i>=m) or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
*         
* * * * * 
        * 
* * * * *
"""
'--------------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
    *     
    *     
    *     
    * 
"""
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
*       * 
*       * 
*       * 
*       * 
* * * * * 
"""
'------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
*       * 
  *   *   
    *     
  *   *   
*       * 
"""
'------------------------------------------'
"""n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()"""
"OUTPUT"
"""
* * * * * 
      *   
    *     
  *       
* * * * * 
"""