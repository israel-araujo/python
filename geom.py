class Retangulo(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.__area = x * y

	def obter_area(self):
		return self.__area
				