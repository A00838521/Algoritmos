def algoritmo_warshall(matriz_adyacencia, nodos):
    n = len(matriz_adyacencia)
    clausura = [fila[:] for fila in matriz_adyacencia]
    
    for k in range(n):
        print(f"Iteración {k+1}: Usando nodo '{nodos[k]}' como intermedio")
        
        for i in range(n):
            for j in range(n):
                if clausura[i][k] and clausura[k][j]:
                    clausura[i][j] = 1
    
    return clausura

def mostrar_caminos(matriz_clausura, nodos):
    print("RESULTADO FINAL - Caminos existentes:")
    print("=" * 40)
    
    for i in range(len(nodos)):
        destinos = []
        for j in range(len(nodos)):
            if matriz_clausura[i][j] == 1 and i != j:
                destinos.append(nodos[j])
        
        if destinos:
            print(f"{nodos[i]} tiene un camino hacia: {', '.join(destinos)}")
        else:
            print(f"{nodos[i]} no tiene caminos hacia otros nodos")

# Definir el grafo de ejemplo
nodos = ['a', 'b', 'c', 'd']
matriz_adj = [
    [0, 1, 0, 0],  # a -> b
    [0, 0, 0, 1],  # b -> d
    [0, 0, 0, 0],  # c -> ninguno
    [1, 0, 1, 0]   # d -> a, c
]

print("Grafo de ejemplo:")
print("a -> b")
print("b -> d") 
print("c -> (ninguno)")
print("d -> a, c")
print()

matriz_final = algoritmo_warshall(matriz_adj, nodos)
mostrar_caminos(matriz_final, nodos)