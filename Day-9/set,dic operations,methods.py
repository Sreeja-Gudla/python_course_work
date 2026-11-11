Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={34,8,40,12,13,50,56,90,29}
s
{34, 8, 40, 12, 13, 50, 56, 90, 29}
sorted(s)
[8, 12, 13, 29, 34, 40, 50, 56, 90]
len(s)
9
max(s)
90
min(s)
8
sum(s)
332
any(s)
True
all(s)
True
s.add(10)
s
{34, 8, 40, 10, 12, 13, 50, 56, 90, 29}
s.add(300)
s
{34, 8, 40, 10, 12, 13, 300, 50, 56, 90, 29}
s.update({1,4,7})
s
{1, 34, 4, 7, 8, 40, 10, 12, 13, 300, 50, 56, 90, 29}
s.pop()
1
s.pop()
34
s.pop()
4
s
{7, 8, 40, 10, 12, 13, 300, 50, 56, 90, 29}
s.pop()
7
s.pop()
8
s.remove(100)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.remove(100)
KeyError: 100
s.remove(300)
s
{40, 10, 12, 13, 50, 56, 90, 29}
s.discard(50)
s.discard(50)
s
{40, 10, 12, 13, 56, 90, 29}
s.clear()
s
set()
a={1,2,3,4}
a
{1, 2, 3, 4}
b=a
b.add(7)
a
{1, 2, 3, 4, 7}
b
{1, 2, 3, 4, 7}
c=a.copy()
c.add(10)
c
{1, 2, 3, 4, 7, 10}
a
{1, 2, 3, 4, 7}
d={}
d={1:1,2.2}
SyntaxError: incomplete input
d={1:1,2:2}
d
{1: 1, 2: 2}
typ(d)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    typ(d)
NameError: name 'typ' is not defined. Did you mean: 'type'?
type(d)
<class 'dict'>
# mutable ordered heterogenuous
# mutable ordered heterogenuous dynamic size
d
{1: 1, 2: 2}
d={}
d[1]="int"
d
{1: 'int'}
d[1.1]="float"
d
{1: 'int', 1.1: 'float'}
d[2+3j]="complex"
d
{1: 'int', 1.1: 'float', (2+3j): 'complex'}
d['str']="string"
d
{1: 'int', 1.1: 'float', (2+3j): 'complex', 'str': 'string'}
d[(1,2,3)]="Tuple"
d
{1: 'int', 1.1: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3): 'Tuple'}
d[False]='bool'
d
{1: 'int', 1.1: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3): 'Tuple', False: 'bool'}
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
d[{1,2}]='set'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d[{1,2}]='set'
TypeError: unhashable type: 'set'
d[{1:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d[{1:2}]='dict'
TypeError: unhashable type: 'dict'
d
{1: 'int', 1.1: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3): 'Tuple', False: 'bool'}
d[1]=1
d
{1: 1, 1.1: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3): 'Tuple', False: 'bool'}
d.clear()
d
{}
d[1]=1
d[2]=12.2
d[3]=2+4j
d[4]='str'
d[5]=[1,2]
d[6]=(1,2)
d[7]={2,33}
d[8]={1:2}
d[9]=False
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {33, 2}, 8: {1: 2}, 9: False}
d[10]=1
d[12]=1
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {33, 2}, 8: {1: 2}, 9: False, 10: 1, 12: 1}
d[2]
12.2
d[4]
'str'
d[6]
(1, 2)
d[8]
{1: 2}
d[13]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d[13]
KeyError: 13
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {33, 2}, 8: {1: 2}, 9: False, 10: 1, 12: 1}
d.get(13)
d.get(7)
{33, 2}
d.get(18)
d.get(18,'key is not there')
'key is not there'
d.get(30,'key is not there')
'key is not there'
d.get(7,'key is not there')
{33, 2}
'str' in d
False
i in d
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    i in d
NameError: name 'i' is not defined. Did you mean: 'id'?
1 in d
True
12.2 in d
False
12 in d
True
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {33, 2}, 8: {1: 2}, 9: False, 10: 1, 12: 1}
d[8]='dict'
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 12: 1}
d[5]=3
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: 3, 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 12: 1}
d[13]=100
d[14]=200
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: 3, 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 12: 1, 13: 100, 14: 200}
d.update(15:500,16:600})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
d.update({15:500,16:600})
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: 3, 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 12: 1, 13: 100, 14: 200, 15: 500, 16: 600}
d.popitem()
(16, 600)
d.poopitem()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    d.poopitem()
AttributeError: 'dict' object has no attribute 'poopitem'. Did you mean: 'popitem'?
d.popitem()
(15, 500)
d
{1: 1, 2: 12.2, 3: (2+4j), 4: 'str', 5: 3, 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 12: 1, 13: 100, 14: 200}
d.poop(2)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    d.poop(2)
AttributeError: 'dict' object has no attribute 'poop'. Did you mean: 'pop'?
d.pop(2)
12.2
d.pop(12)
1
d
{1: 1, 3: (2+4j), 4: 'str', 5: 3, 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 13: 100, 14: 200}
del d[5]
d
{1: 1, 3: (2+4j), 4: 'str', 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 13: 100, 14: 200}
del d[8]
d
{1: 1, 3: (2+4j), 4: 'str', 6: (1, 2), 7: {33, 2}, 9: False, 10: 1, 13: 100, 14: 200}
d.clear()
d
{}
d={1: 1, 3: (2+4j), 4: 'str', 5: 3, 6: (1, 2), 7: {33, 2}, 8: 'dict', 9: False, 10: 1, 13: 100, 14: 200}
d.keys()
dict_keys([1, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14])
d.values()
dict_values([1, (2+4j), 'str', 3, (1, 2), {33, 2}, 'dict', False, 1, 100, 200])
d.items()
dict_items([(1, 1), (3, (2+4j)), (4, 'str'), (5, 3), (6, (1, 2)), (7, {33, 2}), (8, 'dict'), (9, False), (10, 1), (13, 100), (14, 200)])
len(d)
11
sorted(d)
[1, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14]
min(d)
1
max(d)
14

a={1:2,3:4}
b=a
b[12]='sri'
a
{1: 2, 3: 4, 12: 'sri'}
b
{1: 2, 3: 4, 12: 'sri'}
c=a.copy()
c[3]=4
c
{1: 2, 3: 4, 12: 'sri'}
a
{1: 2, 3: 4, 12: 'sri'}
c[7]=2
c
{1: 2, 3: 4, 12: 'sri', 7: 2}
a
{1: 2, 3: 4, 12: 'sri'}
d=dict.fromkeys(['a','b','c','d']=0)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
d=dict.fromkeys(['a','b','c','d'],0)

d
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
d.setdefault('a
             
SyntaxError: incomplete input
d.setdefault('a')
             
0
d.setdefault('h')
             
d
             
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None}
d.setdefault('K',1)
             
1
d
             
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None, 'K': 1}
d.setdefault('c',1)
...              
0
>>> d
...              
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None, 'K': 1}
>>> s=frozenset({1,2,3})
...              
>>> s
...              
frozenset({1, 2, 3})
>>> len(s)
...              
3
>>> max(s)
...              
3
>>> min(s)
...              
1
>>> type(s)
...              
<class 'frozenset'>
