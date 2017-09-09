#-*- coding: UTF-8 -*-

#  don´t forget 
#  from models import Perfil  on cmd 
#  o self é uma referência ao objeto que criamos a partir da classe!
#  Logo, o self do objeto prefil1 não é o mesmo self do objeto perfil2! Cada objeto criado a partir de nossa classe terá seu próprio self criado pelo Python! Mistério explicado.

#Os decorators que fazem um método ser estático, ou seja, de classe são dois:
#@staticmethod e @classmethod cada um com suas particularidades.

class Perfil(object):
	'classe padrao para perfis de usuarios'
	def __init__(self, nome,telefone,empresa):
		if(len(nome) < 3):
			raise ArgumentoInvalidoError('nome deve ter pelo menos 3 caracteres')
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0
		

	def imprime(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s, curtidas: %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
						
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			if(len(valores) is not 3):
				raise ValueError('Uma linha do arquivo %s deve ter 3 valores' % nome_arquivo)
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis			
		

class Data(object):
   def __init__(self, dia, minutos, mes, ano):
      self.dia = dia
      self.minutos = minutos
      self.mes = mes
      self.ano = ano

   def imprime(self):
      print '%s/%s/%s/%s' % (self.dia, self.minutos, self.mes, self.ano)


class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime(self):
        imc = self.peso / (self.altura **2)
        print 'O IMC de %s e : %s ' %(self.nome, imc)      




class Perfil_Vip(Perfil):
	'classe padrao para perfis de usuarios vips'
	def __init__(self, nome,telefone,empresa,apelido=''):
		super(Perfil_Vip, self).__init__(nome,telefone,empresa)
		self.apelido = apelido

	def function():
		pass

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10


class ArgumentoInvalidoError(Exception):
	def __init__(self, mensagem):
		self.mensagem
	def __str__(self):
		return repr(self.mensagem)
		


	
      

				
						

