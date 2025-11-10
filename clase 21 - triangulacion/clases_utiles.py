
# seguramente necesitaras estas librerias
import math
import matplotlib.pyplot as plt


def lee_archivo(archivo):
	f = open(archivo, "r")
	contenido = f.read()
	f.close()

	lines = contenido.split("\n")
	n = int(lines[0])
	aux = [ list(map(float, lines[i].split("\t")))  for i in range(1, len(lines)-1 )]

	points = []
	for a in aux: 
		points.append(Punto(a[0], a[1]))

	return n, points


class Punto:
	def __init__ ( self, x, y ):
		self.x = x
		self.y = y

	def show(self):
		return [self.x, self.y]


class Segmento:
	def __init__ ( self, A, B ):
		self.A = A
		self.B = B

	def show(self):
		return [self.A.x,self.A.y, self.B.x,self.B.y]


class Triangulo:
	def __init__ ( self, puntos ):
		self.puntos = puntos
		s1 = Segmento( puntos[0],  puntos[1])
		s2 = Segmento( puntos[1],  puntos[2])
		s3 = Segmento( puntos[2],  puntos[0])
		self.lados = [s1, s2, s3]

		# darle valores a centro y radio es el problema 2
		self.centro = None
		self.radio = None 



n, points = lee_archivo('instancias/puntos-n10.txt')

