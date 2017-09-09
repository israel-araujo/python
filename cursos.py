# -*- coding: utf-8 -*-

class disciplinas(object):
	def __init__(self, nome_curso, tempo_duracao, valor, instrutor):
		self.nome_curso = nome_curso
		self.tempo_duracao = tempo_duracao
		self.valor = valor
		self.instrutor = instrutor
	def display(self):
		print ' nome_do_curso: %s, tempo_de_duracao_do_curso: %s , valor_do_curso: %s, professor: %s' % (self.nome_curso, self.tempo_duracao, self.valor, self.instrutor)