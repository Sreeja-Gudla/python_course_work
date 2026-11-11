Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[12,4,56,34,56,2,33,76,90,35,52,88,89,14]
l
[12, 4, 56, 34, 56, 2, 33, 76, 90, 35, 52, 88, 89, 14]
l.pop()
14
l.pop()
89
l
[12, 4, 56, 34, 56, 2, 33, 76, 90, 35, 52, 88]
l.pop(0)
12
l
[4, 56, 34, 56, 2, 33, 76, 90, 35, 52, 88]
l.pop(5)
33

l
[4, 56, 34, 56, 2, 76, 90, 35, 52, 88]
l.pop(8)
52
l
[4, 56, 34, 56, 2, 76, 90, 35, 88]
l.remove(2)
l
[4, 56, 34, 56, 76, 90, 35, 88]
l.remove(90)
l.remove(56)
l
[4, 34, 56, 76, 35, 88]
del l[2]
l
[4, 34, 76, 35, 88]
del l[4]
l
[4, 34, 76, 35]
l.clear()
l
[]
l=[12,4,56,34,56,2,33,76,90,35,52,88,89,14]
l
SyntaxError: multiple statements found while compiling a single statement
l=[12,4,56,34,56,2,33,76,90,35,52,88,89,14]
l
[12, 4, 56, 34, 56, 2, 33, 76, 90, 35, 52, 88, 89, 14]
l=[12,4,56,34,56,2,33,76,90,35,12,52,88,89,56,14]
l
[12, 4, 56, 34, 56, 2, 33, 76, 90, 35, 12, 52, 88, 89, 56, 14]
l.count(52)
1
l.count(56)
3
l.index(56)
2
l.index(90)
8
sorted(l)
[2, 4, 12, 12, 14, 33, 34, 35, 52, 56, 56, 56, 76, 88, 89, 90]
l.sort()
l
[2, 4, 12, 12, 14, 33, 34, 35, 52, 56, 56, 56, 76, 88, 89, 90]
l.sort(reverse)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    l.sort(reverse)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
l.reverse()
l
[90, 89, 88, 76, 56, 56, 56, 52, 35, 34, 33, 14, 12, 12, 4, 2]
l.sort(reverse=True)
l
[90, 89, 88, 76, 56, 56, 56, 52, 35, 34, 33, 14, 12, 12, 4, 2]
l.sort()
l
[2, 4, 12, 12, 14, 33, 34, 35, 52, 56, 56, 56, 76, 88, 89, 90]
l.reverse(True)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l.reverse(True)
TypeError: list.reverse() takes no arguments (1 given)
l.sort(reverse=True)
l
[90, 89, 88, 76, 56, 56, 56, 52, 35, 34, 33, 14, 12, 12, 4, 2]
a=[1,2]
c=a
a
[1, 2]
c
[1, 2]
a is c
True
c.append(23)
c.append(5)
l
[90, 89, 88, 76, 56, 56, 56, 52, 35, 34, 33, 14, 12, 12, 4, 2]
a
[1, 2, 23, 5]
c
[1, 2, 23, 5]
c=a.copy()
c.append(4)
c
[1, 2, 23, 5, 4]
a
[1, 2, 23, 5]
l
[90, 89, 88, 76, 56, 56, 56, 52, 35, 34, 33, 14, 12, 12, 4, 2]
any(l)
True
all(l)
True
k=[1,2,3,0]
any(k)
True
all(k)
False
k=[0,0.0,'',[],()]
any(k)
False
all(k)
False
l.sum()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l.sum()
AttributeError: 'list' object has no attribute 'sum'
sum(l)
709
##tuple
#immutable ordered allow_duplicates heterogenous fixed_size
t=()
t=tuple()
t=(1,2,3)
t=tuple((1,2,3,4))
t
(1, 2, 3, 4)
type(t)
<class 'tuple'>
t=1,2,3,4
t
(1, 2, 3, 4)
t(1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
t=(1)
t
1
t=(1,)
t
(1,)
t=(1,2,3,4,1,1,1,1,1)
t
(1, 2, 3, 4, 1, 1, 1, 1, 1)
t=(1,2.0,3+7j,'sri',[1,2,3],(1,2,3),{3,4,5},{1:2,3:4})
t
(1, 2.0, (3+7j), 'sri', [1, 2, 3], (1, 2, 3), {3, 4, 5}, {1: 2, 3: 4})
Traceback (most recent call last):
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t
(1, 2.0, (3+7j), 'sri', [1, 2, 3], (1, 2, 3), {3, 4, 5}, {1: 2, 3: 4})
t=(1,2,3)
t
(1, 2, 3)
a,b,c=t
a
1
b
2
c
3
a,b,c,d=(1,4,3,2)
a
1
b
4
c
3
d
2
t=(1,2.0,3+7j,'sri',[1,2,3],(1,2,3),{3,4,5},{1:2,3:4})

t
(1, 2.0, (3+7j), 'sri', [1, 2, 3], (1, 2, 3), {3, 4, 5}, {1: 2, 3: 4})
t.append(2)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    t.append(2)
AttributeError: 'tuple' object has no attribute 'append'
t[4}].append(4)
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
t[4].append(4)
t
(1, 2.0, (3+7j), 'sri', [1, 2, 3, 4], (1, 2, 3), {3, 4, 5}, {1: 2, 3: 4})
t[3]
'sri'
len(t)
8
a=(1,2,3,4)
b=(7,3,9)
a+b
(1, 2, 3, 4, 7, 3, 9)
a*2
(1, 2, 3, 4, 1, 2, 3, 4)
t
(1, 2.0, (3+7j), 'sri', [1, 2, 3, 4], (1, 2, 3), {3, 4, 5}, {1: 2, 3: 4})
t[2]
(3+7j)
t[6]
{3, 4, 5}
t[-1]
{1: 2, 3: 4}
t[:5]
(1, 2.0, (3+7j), 'sri', [1, 2, 3, 4])
t[::-1]
({1: 2, 3: 4}, {3, 4, 5}, (1, 2, 3), [1, 2, 3, 4], 'sri', (3+7j), 2.0, 1)
t[-2:]
({3, 4, 5}, {1: 2, 3: 4})
t[3:7]
('sri', [1, 2, 3, 4], (1, 2, 3), {3, 4, 5})
1in t
True
10 not in t
True
10 in t
False
len(t)
8
t
(1, 2.0, (3+7j), 'sri', [1, 2, 3, 4], (1, 2, 3), {3, 4, 5}, {1: 2, 3: 4})
min(t)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'complex' and 'int'
t=[12,4,56,34,56,2,33,76,90,35,52,88,89,14]
min(t)
2
max(t)
90
len(t)
14
count(56)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    count(56)
NameError: name 'count' is not defined. Did you mean: 'round'?
count(2)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    count(2)
NameError: name 'count' is not defined. Did you mean: 'round'?
t.count(2)
1
t.count(56)
2
any(t)
True
all(t)
True
sum(t)
641

s={90,3,4,67,27,98}
set=set()
s=set()
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    s=set()
TypeError: 'set' object is not callable
set
set()
s=set(1,2,3)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s=set(1,2,3)
TypeError: 'set' object is not callable
t=set()
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    t=set()
TypeError: 'set' object is not callable
s={1,2,3,5}
s
{1, 2, 3, 5}
s={90,3,4,67,27,98}
s
{98, 67, 3, 4, 90, 27}
s={1,2,1,1,1,1,1}
s
{1, 2}
#unordered no_duplicates mutable heterogenous dynamicsize
s.add(1)
s.add(1.3)
s
{1, 2, 1.3}
s.add('srii')
s.add(2+5j)
s
{1, 2, 1.3, (2+5j), 'srii'}
s.add((1,2,4))
s
{1, 2, 1.3, (2+5j), (1, 2, 4), 'srii'}
s.add(False)
s
{False, 1, 2, 1.3, (2+5j), (1, 2, 4), 'srii'}
s.add([12,33,4])
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    s.add([12,33,4])
TypeError: unhashable type: 'list'
#we cannot have list,set,dictionary inside a set
a={5,4,6,2,7}
a
{2, 4, 5, 6, 7}
b={1,2,8,4,6,7,5}
a
{2, 4, 5, 6, 7}
4 in a
True
5 in b
True
3 in a
False
a|b
{1, 2, 4, 5, 6, 7, 8}
a&b
{2, 4, 5, 6, 7}
>>> a^b
{1, 8}
>>> a-b
set()
>>> a
{2, 4, 5, 6, 7}
>>> b
{1, 2, 4, 5, 6, 7, 8}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({99,100})
True
>>> a
{2, 4, 5, 6, 7}
>>> {2}.issubset(b)
True
>>> {100,3}.issubset(b)
False
>>> a.issubset(b)
True
>>> {1,2,3,4,5,6,7,8,9,10}.issuperset(a)
True
