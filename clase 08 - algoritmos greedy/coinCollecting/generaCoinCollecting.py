

# instancias de coin-collecting

import random



#	Cada instancia contiene una linea con el numero de monedas, 
#	seguida de una matriz n * n  con las monedas en cada celda

def genera_coins(n):

	monedas = [0, 1, 2, 5]	# valores porsibles, 0 es sin moneda

	matrix = [[ random.randint(0, len(monedas) ) for i in range(n) ]  for j in range(n) ]
	matrix[0][0] = 0

	for m in matrix:		
		print(m)

	f = open("coins-n"+ str(n)+ ".txt", "w")

	f.write(str(n) +  "\n")
	for fila in matrix:
		for x in fila:
			f.write( str(x) + "\t")
		f.write("\n")
	f.close()


genera_coins(5)
genera_coins(10)
genera_coins(20)
genera_coins(100)


