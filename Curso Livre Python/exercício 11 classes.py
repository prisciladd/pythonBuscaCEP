Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/pessoas.py 
>>> from pessoas import Pessoa
>>> p=Pessoa()
>>> type(p)
<class 'pessoas.Pessoa'>
>>> p.nome='Joao'
>>> p.nome
'Joao'
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/pessoas.py 
>>> form pessoas import Pessoa
SyntaxError: invalid syntax
>>> p=Pessoa()
>>> from pessoas import Pessoa
>>> p=Pessoa()
>>> p.salvar()
Salvando
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/pessoas.py 
>>> from pessoas import Pessoa
>>> p=Pessoa()
>>> p.nome='Ana'
>>> p.nome
'Ana'
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/pessoas.py 
>>> from pessoas import Pessoa
>>> p=Pessoa()
>>> p.nome='Maria'
>>> p.salvar()
Salvando Maria
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/pessoas.py 
>>> from pessoas import Pessoas
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from pessoas import Pessoas
ImportError: cannot import name 'Pessoas' from 'pessoas' (C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python\pessoas.py)
>>> p=Pessoa()
>>> p.nome='José'
>>> p.salvar('João')
Salvando João
>>> 
