Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista=[1,2,3,4,5]
>>> lista
[1, 2, 3, 4, 5]
>>> lista[ :1]
[1]
>>> lista[ :1]
[1]
>>> lista[1]
2
>>> forx in lista: print (x)
SyntaxError: illegal target for annotation
>>> for in lista: print (x)
SyntaxError: invalid syntax
>>> for x in lista: print (x)

1
2
3
4
5
>>> lista[1,'Antonio',3.14,'Nova String',True]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    lista[1,'Antonio',3.14,'Nova String',True]
TypeError: list indices must be integers or slices, not tuple
>>> for x in lista: print (x)

1
2
3
4
5
>>> lista=[1,'Antonio',3.14,'Nova String',True]
>>> for x in lista: print (x)

1
Antonio
3.14
Nova String
True
>>> lista[2]
3.14
>>> lista[2]='PI'
>>> lista
[1, 'Antonio', 'PI', 'Nova String', True]
>>> lista.append('Novo valor')
>>> lista
[1, 'Antonio', 'PI', 'Nova String', True, 'Novo valor']
>>> lista.pop()
'Novo valor'
>>> lista
[1, 'Antonio', 'PI', 'Nova String', True]
>>> lista.pop()
True
>>> lista.pop()
'Nova String'
>>> lista
[1, 'Antonio', 'PI']
>>> lista.remove('Antonio')
>>> lista
[1, 'PI']
>>> lista.insert(2,'insert')
>>> lista
[1, 'PI', 'insert']
>>> lista.insert(0, 'Inicio')
>>> lista
['Inicio', 1, 'PI', 'insert']
>>> lista.reverse()
>>> lista
['insert', 'PI', 1, 'Inicio']
>>> lista.sort()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lista.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> lista.remove(1)
>>> lista
['insert', 'PI', 'Inicio']

>>> lista.sort()
>>> lista
['Inicio', 'PI', 'insert']
>>> lista.sort()
>>> lista
['Inicio', 'PI', 'insert']
>>> lista.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    lista.sort(reverse=true)
NameError: name 'true' is not defined
>>> lista.sort(reverse= True)
>>> lista
['insert', 'PI', 'Inicio']
>>> tupla=(3,4, 'nome')
>>> tupla
(3, 4, 'nome')
>>> tupla2=3,5, 'nome','sobrenome'
>>> tupla2
(3, 5, 'nome', 'sobrenome')
>>> s=set()
>>> s
set()
>>> s.add(1)
>>> s
{1}
>>> s.add(1,12)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.add(1,12)
TypeError: add() takes exactly one argument (2 given)
>>> s.add(12)
>>> set
<class 'set'>
>>> s
{1, 12}
>>> s.pop()
1
>>> s
{12}
>>> s.add(34)
>>> s
{34, 12}
>>> s.pop()
34
>>> s
{12}
>>> s.add(34,565,345,)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.add(34,565,345,)
TypeError: add() takes exactly one argument (3 given)
>>> s.add(32)
>>> s.add(32)
>>> s
{32, 12}
>>> s.add(321)
>>> s
{32, 321, 12}
>>> s.remove(321)
>>> a
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
{32, 12}
>>> d={}
>>> d
{}
>>> type(d)
<class 'dict'>
>>> d['nome']='Marcos'
>>> d['sobrenome']='Almeida'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida'}
>>> d['data_nascimeto']='18/05/1979'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida', 'data_nascimeto': '18/05/1979'}
>>> d['data_nascimento']='18/05/1979'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida', 'data_nascimeto': '18/05/1979', 'data_nascimento': '18/05/1979'}
>>> d.remove('data_nascimeto')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d.remove('data_nascimeto')
AttributeError: 'dict' object has no attribute 'remove'
>>> d.pop('telefone')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    d.pop('telefone')
KeyError: 'telefone'
>>> d.pop('data_nascimeto')
'18/05/1979'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida', 'data_nascimento': '18/05/1979'}
>>> d.popitem()
('data_nascimento', '18/05/1979')
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida'}
>>> d.values()
dict_values(['Marcos', 'Almeida'])
>>> d.keys()
dict_keys(['nome', 'sobrenome'])
>>> 
