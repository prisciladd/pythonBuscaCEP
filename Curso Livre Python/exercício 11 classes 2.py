Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py from ca
>>> from carros import Carro
>>> c=Carro()print(c.caminho)
SyntaxError: invalid syntax
>>> c=Carro()print(c.caminho)
SyntaxError: invalid syntax
>>> c=Carro()
>>> c.andar()
Andando pela Rua
>>> print(c.caminho)
Rua
>>> c.caminho='Estrada'
>>> c.caminho
'Estrada'
>>> c.andar()
Andando pela Rua
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py 
>>> from carros import Carro
>>> c= Carro()
>>> c.caminho
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py 
>>> from carros import Carro
>>> c=Carro('Ponte')
>>> c.caminho
'Ponte'
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py 
>>> from carros import Carro
>>> c=carro('Ponte')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c=carro('Ponte')
NameError: name 'carro' is not defined
>>> c=Carro('Ponte')
>>> c.andar()
Andando pela Ponte
>>> c.caminho='Praia'
>>> c.andar()
Andando pela Praia
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py 
>>> from carros import Fusca
>>> f=Fusca('Avenida')
>>> type(f)
<class 'carros.Fusca'>
>>> f.andar()
Andando pela Avenida
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py 
>>> from carros import Fusca
>>> f= Fusca('Praia')
>>> f.andar()
Andando pela Praia
>>> f.correr()
Andando pela pista
>>> 
 RESTART: C:/Users/Pri&Le/Documents/IMPACTA SI NOTURNO/2º SEM 2019 1º SEM CURSO/Curso Livre Python/carros.py 
>>> from carros import Ferrari
>>> ferrari=Ferrari('Avenida')
>>> ferrari.andar()
Correndo muito
>>> 
