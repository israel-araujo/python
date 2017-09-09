# -*- coding: UTF-8 -*-

import re

def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):    
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover e  0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes) 

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            procurar(nomes)
        if(escolha == '5'):
            procurar(nomes)            

        if(nome_a_alterar in nomes):
            posicao = nomes.index(nome_a_alterar)
            print 'Digite novo nome'
            nome_novo = raw_input()
            nomes[posicao] = nome_novo
            alterar(nomes)



def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual o nome que voce quer remover'
    nome = raw_input()
    nomes.remove(nomes)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_alterar = raw_input()

def procurar(nomes):
    print 'digite nome a ser procurado'
    nome_a_procurar = raw_input()

    if(nome in nomes):
    print 'nome %s  esta cadastrado' %(nome)
    else:
    print 'nome %s nao esta cadastrado' %(nome)

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = '-'.join(nomes)
    resultados = re.findall(regex,nomes_concatenados)
    print(resultados)


menu()