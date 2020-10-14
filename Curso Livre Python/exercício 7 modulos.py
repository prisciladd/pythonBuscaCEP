Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random
<built-in method random of Random object at 0x02606018>
>>> random.random ()
0.9511804581106421
>>> random.random ()
0.19427794764196415
>>> random.random ()
0.21951971287613004
>>> random.random ()
0.7580066398976429
>>> 
random.randit(10,20)
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    random.randit(10,20)
AttributeError: module 'random' has no attribute 'randit'
>>> random.randint(10,20)
17
>>> random.randint(10,20)
16
>>> random.randint(10,20)
13
>>> random.randint(10,20)
13
>>> x= ['fusca', 'uno','pic up','kombi']
>>> random.choice(x)
'fusca'
>>> random.choice(x)
'kombi'
>>> random.choice(x)
'pic up'
>>> random.choice(x)
'uno'
>>> random.choice(x)
'fusca'
>>> random.shuffle (x)
>>> random.shuffle(x)
>>> x= ['fusca', 'uno','pic up','kombi']
>>> random.shuffle(x)
>>> 
>>> x['fusca', 'uno','pic up','kombi']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x['fusca', 'uno','pic up','kombi']
TypeError: list indices must be integers or slices, not tuple
>>> random.shuffle(x)
>>> x
['fusca', 'uno', 'pic up', 'kombi']
>>> random.shuffle(x)
>>> random.shuffle(x)
>>> x
['pic up', 'uno', 'fusca', 'kombi']
>>> x= ['fusca', 'uno','pic up','kombi']
>>> random.shuffle(x)
>>> x
['kombi', 'fusca', 'pic up', 'uno']
>>> import string
>>> string.ponctuation
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    string.ponctuation
AttributeError: module 'string' has no attribute 'ponctuation'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.digits
'0123456789'
>>> string.hexadigits
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    string.hexadigits
AttributeError: module 'string' has no attribute 'hexadigits'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> string.capwords ('teste de captalize no curso de python')
'Teste De Captalize No Curso De Python'
>>> 
