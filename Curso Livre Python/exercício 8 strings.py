Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'Priscila'" Da DAlt"''' '''
'Priscila Da DAlt '
>>> 'Priscila'" Da Dalt"''' '''
'Priscila Da Dalt '
>>> ''' Texto multilinha'''
' Texto multilinha'
>>> ''' Texto multilinha
para teste
na aula de Python '''
' Texto multilinha\npara teste\nna aula de Python '
>>> 'Texto para ser fatiado' [0:10]
'Texto para'
>>> 'Texto para ser fatiado' [3:10]
'to para'
>>> 'Texto para ser fatiado' [3:]
'to para ser fatiado'
>>> 'Texto para ser fatiado' [:10]
'Texto para'
>>> 'Texto para ser fatiado' [:10:3]
'Ttpa'
>>> 'Fatiamento com valor negativo'[ : :-1]
'ovitagen rolav moc otnemaitaF'
>>> 'Fatiamento com valor negativo'[ :-4]
'Fatiamento com valor nega'
>>> 'Fatiamento com valor negativo'[5 :-4]
'mento com valor nega'
>>> nome='arara'
>>> nome==nome[ : :-1]
True
>>> nome='priscila'
>>> nome==nome[ : :-1]
False
>>> nome='ana'
>>> nome==nome[ : :-1]
True
>>> nome='Marcos'
>>> nome='B'+nome[1:]
>>> nome
'Barcos'
>>> 
nome.startswith('B')
True
>>> nome.startswith('b')
False
>>> nome.endwith('s')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    nome.endwith('s')
AttributeError: 'str' object has no attribute 'endwith'
>>> nome.endswith('s')
True
>>>  True
 
SyntaxError: unexpected indent
>>> nome.endswith('d')
False
>>> nome.replace('r', '3')
'Ba3cos'
>>> nome
'Barcos'
>>> nome= nome.replace('r', '3')
>>> nome
'Ba3cos'
>>> texto='Testando split no python'
>>> s=texto.split()
>>> s
['Testando', 'split', 'no', 'python']
>>> texto='Testando;novos;delimitadores'
>>> s=texto.split(;)
SyntaxError: invalid syntax
>>> s
['Testando', 'split', 'no', 'python']
>>> s=texto.split(';')
>>> s
['Testando', 'novos', 'delimitadores']
>>> data='27''07''1987'
>>> '/'.join(data)
'2/7/0/7/1/9/8/7'
>>> '/'.join(data)data
SyntaxError: invalid syntax
>>> data='27','07','1987'
>>> '/'.join(data)
'27/07/1987'
>>> 
