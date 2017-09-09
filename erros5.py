# -*- coding: UTF-8 -*-
try:
    arquivo = open('texto1.csv', 'r')
    for linha in arquivo:
        print linha
except:
	print 'Arquivo não encontrado'
print 'FIM'