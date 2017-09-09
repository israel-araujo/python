# -*- coding: UTF-8 -*-

#erros.py
try:
        open('nao_existe.txt','r')
        print('O arquivo foi aberto')
        arquivo.close()
except IOError as erro:
        print('except definimos o tipo de exceção que pode acontecer e qual é o tratamento')