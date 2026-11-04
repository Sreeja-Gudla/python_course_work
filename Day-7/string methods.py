Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='Python Programming'
s.startswith('p')
False
KeyboardInterrupt
s.startswith('P')
True
s.startswith('pyt')
False
s.startswith('Pyt')
True
s.startswith('ing')
False
s.endswith('ing')
True
's'.islower()
True
'p'.isupper()
False
'P'.isupper()
True
'codeganan'.isaplha()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    'codeganan'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
'codeganan'.isalpha()
True
'codeganan@'.isalpha()
False
'codeganan'.isalpha()
True
'code123'.isalnum()
True
'code12@'.isalnum()
False
'sri'.isalnum()
True
'123'.isalnum()
True
s
'Python Programming'
s.istitle()
True
'myvar'.isidentifier()
True
'my@var'.isidentifier()
False
' '.isspace()
True
'             hi '.isspace()
False
'123'.isdecimal()
True
'1234'.isnumeric()
True
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d'.srplit('-')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    'a-b-c-d'.srplit('-')
AttributeError: 'str' object has no attribute 'srplit'. Did you mean: 'split'?
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
KeyboardInterrupt
'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
s="""
hello
world
python
"""
s
'\nhello\nworld\npython\n'
s.splitlines()
['', 'hello', 'world', 'python']
l=['a','b','c',]
'-'.join(l)
'a-b-c'
'@'.join(l)
'a@b@c'
'*'.join(l)
'a*b*c'
'_'.join(l)
'a_b_c'
>>> ' '.join(l)
'a b c'
>>> s.partition('b')
('\nhello\nworld\npython\n', '', '')
>>> s='a-b-c-d'
>>> s.partition('b')
... 
('a-', 'b', '-c-d')
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> 'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
>>> 'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
>>> s='hello'
>>> s.encode()
b'hello'
>>> t='hello 😀'
>>> t.encode()
b'hello \xf0\x9f\x98\x80'
>>> b'hello \xf0\x9f\x98\x80'.decode()
'hello 😀'
