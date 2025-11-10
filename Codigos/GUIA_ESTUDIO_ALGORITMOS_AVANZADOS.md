# GUÍA DE ESTUDIO: ALGORITMOS AVANZADOS

## Para Examen - Guía Completa con Ejemplos y Diagramas ASCII

---

## TABLA DE CONTENIDOS

1. [Algoritmos de Fuerza Bruta](#1-algoritmos-de-fuerza-bruta)
2. [Decrease and Conquer](#2-decrease-and-conquer)
3. [Divide y Vencerás](#3-divide-y-venceras)
4. [Programación Dinámica](#4-programacion-dinamica)
5. [Backtracking](#5-backtracking)
6. [Branch and Bound](#6-branch-and-bound)
7. [Algoritmos Greedy](#7-algoritmos-greedy)
8. [Árboles de Huffman](#8-arboles-de-huffman)
9. [Suffix Trie](#9-suffix-trie)
10. [Problemas Clásicos](#10-problemas-clasicos)

---

## 1. ALGORITMOS DE FUERZA BRUTA

### Concepto Fundamental

La fuerza bruta examina TODAS las soluciones posibles de manera sistemática.

### Características:

- **Complejidad:** Generalmente O(n²) o exponencial
- **Ventajas:** Simple de implementar, siempre encuentra la solución óptima
- **Desventajas:** Ineficiente para grandes datasets

### Problema: Closest Pair (Par Más Cercano)

```yaml
DIAGRAMA ASCII:
    y
    |
  4 |   A     B
    |
  2 |     C
    |
  0 +----------- x
    0   2   4

Distancia A-C = √[(x₁-x₂)² + (y₁-y₂)²]
```

**ALGORITMO:**

```python
def closest_pair_brute_force(points):
    """
    Encuentra la pareja de puntos más cercana usando fuerza bruta
    
    ¿Cómo funciona?
    1. Compara CADA punto con TODOS los demás puntos
    2. Calcula la distancia entre cada par
    3. Guarda el par con la distancia más pequeña
    
    Entrada: lista de puntos [(x1,y1), (x2,y2), ...]
    Salida: (par_más_cercano, distancia_mínima)
    """
    # Inicializar distancia mínima como infinito (cualquier distancia será menor)
    min_dist = float("inf")
    closest_pair = None
    
    # Examinar TODOS los pares posibles O(n²)
    # Primer bucle: seleccionar el primer punto del par
    for i in range(len(points)):
        # Segundo bucle: seleccionar el segundo punto (evita repetir pares)
        # Empezamos en i+1 para no comparar un punto consigo mismo
        for j in range(i + 1, len(points)):
            # Calcular distancia euclidiana entre los dos puntos actuales
            dist = euclidean_distance(points[i], points[j])
            
            # Si encontramos una distancia menor, actualizamos nuestros registros
            if dist < min_dist:
                min_dist = dist  # Nueva distancia mínima
                closest_pair = (points[i], points[j])  # Nueva pareja más cercana
    
    # Retornamos la pareja más cercana y su distancia
    return closest_pair, min_dist
```

**COMPLEJIDAD:** O(n²) - examina n(n-1)/2 pares

**¿Por qué O(n²)?**

- Con n puntos, el primer bucle ejecuta n veces
- El segundo bucle ejecuta (n-1) + (n-2) + ... + 1 = n(n-1)/2 veces
- Total: aproximadamente n²/2 comparaciones

```python
# Función auxiliar para calcular distancia euclidiana
def euclidean_distance(point1, point2):
    """
    Calcula la distancia euclidiana entre dos puntos
    
    ¿Qué es la distancia euclidiana?
    Es la distancia "en línea recta" entre dos puntos, como si fuera
    la hipotenusa de un triángulo rectángulo.
    
    Fórmula: √[(x₁-x₂)² + (y₁-y₂)²]
    
    Ejemplo: puntos (1,2) y (4,6)
    distancia = √[(1-4)² + (2-6)²] = √[9 + 16] = √25 = 5
    """
    # Extraer coordenadas x e y de cada punto
    x1, y1 = point1[0], point1[1]  # Coordenadas del primer punto
    x2, y2 = point2[0], point2[1]  # Coordenadas del segundo punto
    
    # Aplicar la fórmula de distancia euclidiana paso a paso:
    # 1. Diferencia en x: (x1 - x2)
    # 2. Diferencia en y: (y1 - y2)
    # 3. Elevar ambas al cuadrado y sumar
    # 4. Sacar raíz cuadrada del resultado
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance
```

### Problema: String Matching (Búsqueda de Patrones)

```md
DIAGRAMA ASCII:
Texto:   A B C A B A B C A B
Patrón:  A B A B
         ^
         Comparar carácter por carácter
```

**ALGORITMO:**

```python
def string_matching_brute_force(text, pattern):
    """
    Encuentra todas las posiciones donde aparece un patrón en un texto
    usando el método de fuerza bruta (comparación carácter por carácter)
    
    ¿Cómo funciona?
    1. Para cada posición posible en el texto
    2. Compara el patrón carácter por carácter
    3. Si todos coinciden, guarda esa posición
    
    Ejemplo: text="ABCAB", pattern="AB"
    - Posición 0: AB vs AB ✓ (coincide)
    - Posición 1: BC vs AB ✗
    - Posición 2: CA vs AB ✗  
    - Posición 3: AB vs AB ✓ (coincide)
    Resultado: [0, 3]
    """
    matches = []  # Lista para guardar posiciones donde encontramos el patrón
    n, m = len(text), len(pattern)  # Longitudes del texto y patrón
    
    # Probar cada posición posible donde puede empezar el patrón
    # Solo probamos hasta (n-m) porque después no cabría el patrón completo
    for i in range(n - m + 1):
        match = True  # Asumimos que hay coincidencia hasta que se demuestre lo contrario
        
        # Comparar cada carácter del patrón con el texto
        # Empezamos en la posición i del texto
        for j in range(m):
            # Comparar: texto[i+j] con patrón[j]
            # Si algún carácter no coincide, no hay match en esta posición
            if text[i + j] != pattern[j]:
                match = False
                break  # No necesitamos seguir comparando, ya sabemos que no coincide
        
        # Si llegamos aquí con match=True, significa que todos los caracteres coincidieron
        if match:
            matches.append(i)  # Guardar la posición donde inicia el patrón
    
    # Retornamos lista con todas las posiciones donde aparece el patrón
    return matches
```

**COMPLEJIDAD:** O(n*m) donde n=texto, m=patrón

---

## 2. DECREASE AND CONQUER

### Concepto Fundamental

Reduce el problema en una unidad en cada iteración.

### Características:

- **Estrategia:** Resolver subproblema de tamaño n-1
- **Típicamente recursivo**
- **Complejidad:** O(log n) en mejores casos

### Problema: Potenciación Rápida

```groovy
DIAGRAMA ASCII:
power(2, 8)
    |
power(2, 4) * power(2, 4)
    |               |
power(2,2)²     power(2,2)²
    |               |
power(2,1)²     power(2,1)²

Reducción: n → n/2 en cada paso
```

**ALGORITMO:**

```python
def power(a, n):
    """
    Calcula a^n usando el algoritmo de potenciación rápida
    
    ¿Por qué es más rápido?
    En lugar de multiplicar 'a' por sí mismo n veces (que sería O(n)),
    dividimos el problema a la mitad en cada paso (que es O(log n)).
    
    Idea clave: 
    - Si n es par: a^n = (a^(n/2))²
    - Si n es impar: a^n = (a^(n/2))² * a
    
    Ejemplo: power(2, 8)
    - power(2, 8) = power(2, 4)² = 16² = 256
    - power(2, 4) = power(2, 2)² = 4² = 16  
    - power(2, 2) = power(2, 1)² = 2² = 4
    - power(2, 1) = power(2, 0)² * 2 = 1² * 2 = 2
    - power(2, 0) = 1 (caso base)
    """
    # Caso base: cualquier número elevado a 0 es 1
    if n == 0:
        return 1
    
    # Dividir el problema a la mitad (decrease and conquer)
    # En lugar de calcular a^n directamente, calculamos a^(n/2)
    # Usamos // para división entera (sin decimales)
    half = power(a, n // 2)
    
    # Ahora decidimos cómo usar este resultado según si n es par o impar
    if n % 2 == 0:
        # Si n es par: a^n = (a^(n/2))^2
        # Ejemplo: 2^8 = (2^4)^2 = 16^2 = 256
        return half * half
    else:
        # Si n es impar: a^n = (a^(n/2))^2 * a
        # Ejemplo: 2^9 = (2^4)^2 * 2 = 16^2 * 2 = 256 * 2 = 512
        return half * half * a
```

**COMPLEJIDAD:** O(log n)

---

## 3. DIVIDE Y VENCERÁS

### Concepto Fundamental

Dividir el problema en subproblemas, resolver independientemente, combinar resultados.

### Estructura Típica:

```sh
DIAGRAMA ASCII:
    Problema(n)
       /    \
 Sub1(n/2) Sub2(n/2)
    /  \     /  \
  ...  ... ... ...

Dividir → Conquistar → Combinar
```

### Ejemplos Clásicos:

**Merge Sort:**

```python
def merge_sort(arr):
    """
    Ordena un arreglo usando el algoritmo Merge Sort (divide y vencerás)
    
    ¿Cómo funciona?
    1. DIVIDIR: Partir el arreglo por la mitad
    2. CONQUISTAR: Ordenar recursivamente cada mitad  
    3. COMBINAR: Unir las dos mitades ya ordenadas
    
    Ejemplo: [64, 34, 25, 12]
    - Dividir: [64, 34] y [25, 12]
    - Ordenar: [34, 64] y [12, 25] 
    - Combinar: [12, 25, 34, 64]
    
    ¿Por qué es eficiente?
    - Siempre divide el problema exactamente a la mitad
    - La combinación es O(n) y se hace O(log n) veces
    - Total: O(n log n) que es mucho mejor que O(n²)
    """
    # Caso base: si el arreglo tiene 1 o 0 elementos, ya está ordenado
    if len(arr) <= 1:
        return arr
    
    # PASO 1: DIVIDIR - encontrar el punto medio
    mid = len(arr) // 2  # División entera para obtener índice entero
    
    # PASO 2: CONQUISTAR - ordenar recursivamente cada mitad
    # La recursión se encarga de seguir dividiendo hasta llegar al caso base
    left = merge_sort(arr[:mid])    # Mitad izquierda (desde inicio hasta mid)
    right = merge_sort(arr[mid:])   # Mitad derecha (desde mid hasta final)
    
    # PASO 3: COMBINAR - unir las dos mitades ya ordenadas
    return merge(left, right)       # Función merge une dos arreglos ordenados
```

**COMPLEJIDAD:** O(n log n)

```python
# Función auxiliar merge para combinar dos arreglos ordenados
def merge(left, right):
    """
    Combina dos arreglos ordenados en uno solo ordenado
    Esta es la parte "COMBINAR" de divide y vencerás
    
    ¿Cómo funciona?
    Imagina dos pilas de cartas ordenadas. Siempre tomas la carta 
    más pequeña de la parte superior de cualquiera de las dos pilas.
    
    Ejemplo: left=[1,3,5], right=[2,4,6]
    - Comparar 1 vs 2: tomar 1 → result=[1]
    - Comparar 3 vs 2: tomar 2 → result=[1,2] 
    - Comparar 3 vs 4: tomar 3 → result=[1,2,3]
    - Y así sucesivamente...
    """
    result = []  # Arreglo resultado que contendrá elementos ordenados
    i = j = 0    # Índices para recorrer left y right respectivamente
    
    # Mientras tengamos elementos en ambos arreglos
    while i < len(left) and j < len(right):
        # Comparar el elemento actual de cada arreglo
        if left[i] <= right[j]:
            # El elemento de 'left' es menor o igual, lo tomamos
            result.append(left[i])
            i += 1  # Avanzamos el índice de 'left'
        else:
            # El elemento de 'right' es menor, lo tomamos
            result.append(right[j])
            j += 1  # Avanzamos el índice de 'right'
    
    # Agregar elementos restantes (uno de los arreglos ya se acabó)
    # Solo uno de estos while se ejecutará
    while i < len(left):
        # Quedan elementos en 'left', agregarlos todos
        result.append(left[i])
        i += 1
    
    while j < len(right):
        # Quedan elementos en 'right', agregarlos todos  
        result.append(right[j])
        j += 1
    
    return result  # Arreglo combinado y completamente ordenado
```

---

## 4. PROGRAMACIÓN DINÁMICA

### Concepto Fundamental

Resolver subproblemas una vez y guardar resultados para evitar recálculos.

### Dos Enfoques:

1. **Top-down (Memoización):** Recursivo con tabla de memoria
2. **Bottom-up (Tabulación):** Iterativo construyendo tabla

### Problema: Coin Change

```ini
DIAGRAMA ASCII - Tabla DP:
Monedas: [1, 2, 5]
Cantidad: 4

    j→ 0  1  2  3  4
i ↓    
0      1  0  0  0  0
1[1]   1  1  1  1  1
2[2]   1  1  2  2  3
3[5]   1  1  2  2  3

T[i][j] = formas de hacer cantidad j con primeras i monedas
```

**ALGORITMO (Tabulación):**

```python
def coin_change_dp(coins, amount):
    """
    Calcula el número de formas de hacer una cantidad usando monedas dadas
    usando Programación Dinámica (enfoque tabulación)
    
    ¿Qué es Programación Dinámica?
    En lugar de recalcular los mismos subproblemas una y otra vez,
    los resolvemos una sola vez y guardamos el resultado en una tabla.
    
    Idea clave: T[i][j] = número de formas de hacer cantidad j 
                          usando las primeras i tipos de monedas
    
    Ejemplo: monedas=[1,2], cantidad=3
    - T[1][3] = formas usando solo monedas de 1: 1+1+1 = 1 forma
    - T[2][3] = formas usando monedas de 1 y 2: 1+1+1, 1+2 = 2 formas
    """
    n = len(coins)  # Número de tipos de monedas disponibles
    
    # Crear tabla DP: T[i][j] = formas de hacer cantidad j con primeras i monedas
    # Filas: tipos de monedas (0 a n)
    # Columnas: cantidades (0 a amount)
    T = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    
    # CASO BASE: Hay exactamente 1 forma de hacer cantidad 0 (no usar ninguna moneda)
    for i in range(n + 1):
        T[i][0] = 1  # Primera columna = 1
    
    # Llenar la tabla usando programación dinámica
    # Procesamos fila por fila (tipo de moneda por tipo de moneda)
    for i in range(1, n + 1):          # Para cada tipo de moneda (1 a n)
        for j in range(amount + 1):    # Para cada cantidad posible (0 a amount)
            
            # OPCIÓN 1: No usar la moneda actual (tipo i)
            # Las formas son las mismas que sin esta moneda
            T[i][j] = T[i-1][j]
            
            # OPCIÓN 2: Usar la moneda actual (si es posible)
            if j >= coins[i-1]:  # Solo si la cantidad es suficiente para esta moneda
                # Agregar las formas de hacer (cantidad - valor_moneda) 
                # usando esta misma moneda (por eso es T[i][...], no T[i-1][...])
                T[i][j] += T[i][j - coins[i-1]]
    
    # La respuesta está en la esquina inferior derecha de la tabla
    return T[n][amount]
```

**COMPLEJIDAD:** O(n * amount)

```py
# Ejemplo: coins = [1, 2, 5], amount = 4
# ¿De cuántas formas podemos hacer 4?

def coin_change_ejemplo():
    coins = [1, 2, 5]
    amount = 4
    
    # Respuestas posibles:
    # 1+1+1+1 = 4  (usar moneda de 1, cuatro veces)
    # 1+1+2 = 4    (usar moneda de 1 dos veces, moneda de 2 una vez)  
    # 2+2 = 4      (usar moneda de 2, dos veces)
    # Total: 3 formas diferentes
    
    result = coin_change_dp(coins, amount)
    print(f"Hay {result} formas de hacer {amount} con monedas {coins}")
    
coin_change_ejemplo()  # Output: Hay 3 formas de hacer 4 con monedas [1, 2, 5]
```

```ini
DIAGRAMA ASCII - Tabla DP:
Objetos: [(peso, valor)]
Capacidad: W

    W→ 0  1  2  3  4  5
i ↓    
0      0  0  0  0  0  0
1      0  0  0  V₁ V₁ V₁
2      0  0  V₂ max(...) ...
```

---

## 5. BACKTRACKING

### Concepto Fundamental

Exploración sistemática del espacio de soluciones con retroceso cuando no hay solución viable.

### Estructura del Algoritmo:

```md
DIAGRAMA ASCII - Árbol de Decisiones:
        []
      /    \
   [1]      [0]
   / \      / \
[1,1][1,0][0,1][0,0]
  |    |    |    |
 ...  ...  ... ...

Poda: Si suma > objetivo, retroceder
```

**ALGORITMO GENÉRICO:**

```python
def backtrack(solution, level):
    """
    Algoritmo genérico de backtracking
    
    ¿Qué es backtracking?
    Es como resolver un laberinto: avanzas por un camino, y si llegas
    a un callejón sin salida, retrocedes y pruebas otro camino.
    
    Pasos del algoritmo:
    1. ELEGIR: Seleccionar un candidato para la posición actual
    2. EXPLORAR: Avanzar al siguiente nivel con esa elección
    3. RETROCEDER: Si no hay solución, deshacer la elección y probar otra
    
    Ejemplo: Encontrar subconjunto que sume 5 en [2,3,1]
    - Elegir 2: [2,?,?] → suma parcial = 2
    - Elegir 3: [2,3,?] → suma parcial = 5 ¿Es solución? 
    - Si no funciona, retroceder: [2,?,?] y probar no elegir 3
    """
    # CONDICIÓN DE PARADA: Verificar si hemos completado una solución
    if is_complete(solution):
        # Si la solución es válida (cumple las restricciones), procesarla
        if is_valid(solution):
            process_solution(solution)  # Imprimir, guardar, contar, etc.
        return  # Terminar esta rama de búsqueda
    
    # GENERAR CANDIDATOS: Obtener todas las opciones posibles para este nivel
    for candidate in get_candidates(solution, level):
        
        # PASO 1: ELEGIR - asignar el candidato a la solución parcial
        solution[level] = candidate
        
        # PASO 2: VERIFICAR - ¿esta elección es prometedora? (poda temprana)
        if is_promising(solution, level):
            # PASO 3: EXPLORAR - continuar construyendo la solución
            backtrack(solution, level + 1)
        
        # PASO 4: RETROCEDER - deshacer la elección para probar otras opciones
        # Esto es CRUCIAL: sin esto no podríamos probar otros candidatos
        solution[level] = -1  # Marcar como "indefinido" o "sin asignar"
```

### Problema: Subset Sum

```python
def subset_sum_backtrack(numbers, target):
    """
    Encuentra si existe un subconjunto de números que sume exactamente el objetivo
    usando backtracking
    
    ¿Qué es el problema Subset Sum?
    Dado un conjunto de números, ¿puedo elegir algunos de ellos (subconjunto)
    tal que su suma sea exactamente igual a un valor objetivo?
    
    Ejemplo: numbers=[1,3,5], target=4
    - Subconjuntos posibles: [], [1], [3], [5], [1,3], [1,5], [3,5], [1,3,5]
    - Sus sumas: 0, 1, 3, 5, 4, 6, 8, 9
    - ¿Alguna suma es 4? ¡Sí! [1,3] suma 4
    """
    
    def backtrack(index, current_sum, solution):
        """
        Función recursiva que explora todas las posibilidades
        
        Parámetros:
        - index: posición actual en el arreglo de números
        - current_sum: suma de números elegidos hasta ahora  
        - solution: arreglo que marca qué números hemos elegido
        """
        
        # CASO BASE: Hemos considerado todos los números
        if index == len(numbers):
            # ¿La suma actual es exactamente igual al objetivo?
            return current_sum == target
        
        # PODA INTELIGENTE: Si ya excedimos el objetivo, no hay solución
        # Esta optimización evita explorar ramas innecesarias
        if current_sum > target:
            return False
        
        # DECISIÓN 1: Incluir el número actual en el subconjunto
        solution[index] = 1  # Marcar como "incluido"
        # Llamada recursiva con la suma actualizada
        if backtrack(index + 1, current_sum + numbers[index], solution):
            return True  # ¡Encontramos una solución!
        
        # DECISIÓN 2: No incluir el número actual en el subconjunto  
        solution[index] = 0  # Marcar como "no incluido"
        # Llamada recursiva sin cambiar la suma
        if backtrack(index + 1, current_sum, solution):
            return True  # ¡Encontramos una solución!
        
        # RETROCEDER: Restaurar el estado antes de salir
        # Esto permite que el nivel superior pruebe otras opciones
        solution[index] = -1  # Marcar como "indefinido"
        return False  # No encontramos solución en esta rama
    
    # Inicializar el arreglo de solución
    # -1 = indefinido, 0 = no incluido, 1 = incluido
    solution = [-1] * len(numbers)
    
    # Comenzar la búsqueda desde el índice 0 con suma 0
    return backtrack(0, 0, solution)
```

**COMPLEJIDAD:** O(2ⁿ) en el peor caso

```python
**EJEMPLO PASO A PASO:**
```python
# Ejemplo: numbers = [3, 5, 2], target = 7
# ¿Existe un subset que sume exactamente 7?

def subset_sum_ejemplo():
    numbers = [3, 5, 2] 
    target = 7
    
    # Posibles subsets:
    # [] = 0
    # [3] = 3
    # [5] = 5  
    # [2] = 2
    # [3,5] = 8 (excede target)
    # [3,2] = 5
    # [5,2] = 7  ← ¡SOLUCIÓN ENCONTRADA!
    # [3,5,2] = 10 (excede target)
    
    solution = [-1] * len(numbers)
    found = subset_sum_backtrack(numbers, target)
    print(f"¿Existe subset que suma {target}? {found}")
    if found:
        print("Subset encontrado:", [numbers[i] for i in range(len(numbers)) if solution[i] == 1])

subset_sum_ejemplo()  # Output: ¿Existe subset que suma 7? True
```


---

## 6. BRANCH AND BOUND


Optimización de backtracking usando cotas (bounds) para podar ramas no prometedoras.


1. **Upper Bound:** Cota superior del valor óptimo
2. **Lower Bound:** Mejor solución encontrada hasta ahora
3. **Poda:** Eliminar ramas donde UB ≤ LB

```hs

```md
DIAGRAMA ASCII - Poda por Bounds:
        Nodo[UB=100]
          /      \
   [UB=80]        [UB=60]
     /   \           X (podado porque UB < mejor_conocido=70)
  [UB=75] [UB=45]
```

**ALGORITMO PARA KNAPSACK:**

```python
def branch_and_bound_knapsack(weights, values, capacity):
    """
    Resuelve el problema de la mochila usando Branch and Bound
    
    ¿Qué es Branch and Bound?
    Es como backtracking, pero más inteligente. Usa "cotas" (bounds) para
    podar ramas que definitivamente no pueden dar la solución óptima.
    
    ¿Cómo funciona?
    1. Para cada nodo, calcula el "upper bound" (máximo valor teórico posible)
    2. Si este upper bound es peor que la mejor solución conocida, 
       no explora esa rama (PODA)
    3. Esto evita explorar millones de combinaciones inútiles
    
    Upper Bound = valor actual + valor fraccionario de objetos restantes
    """
    
    def upper_bound(index, current_weight, current_value):
        """
        Calcula la cota superior (upper bound) de forma optimista
        
        ¿Qué es el upper bound?
        Es el MÁXIMO valor que podríamos obtener si pudiéramos cortar
        los objetos en pedazos (relajación fraccionaria).
        
        Obviamente esto no es válido en la mochila 0/1, pero nos da
        una cota superior que usamos para podar.
        """
        # Si ya consideramos todos los objetos, el bound es el valor actual
        if index == len(weights):
            return current_value
        
        remaining_capacity = capacity - current_weight  # Espacio libre
        bound = current_value  # Empezamos con el valor garantizado
        
        # Intentar agregar objetos restantes (de forma fraccionaria si es necesario)
        for i in range(index, len(weights)):
            if weights[i] <= remaining_capacity:
                # Si el objeto cabe completo, lo agregamos
                bound += values[i]
                remaining_capacity -= weights[i]
            else:
                # Si no cabe completo, agregamos una fracción
                # Esto da una estimación OPTIMISTA del valor máximo posible
                bound += (remaining_capacity / weights[i]) * values[i]
                break  # Ya no hay más capacidad
        
        return bound
    
    def branch_and_bound(index, current_weight, current_value, solution):
        """
        Función recursiva principal de branch and bound
        """
        nonlocal best_value, best_solution
        
        # CASO BASE: Hemos considerado todos los objetos
        if index == len(weights):
            # Si esta solución es mejor que la actual, actualizamos
            if current_value > best_value:
                best_value = current_value
                best_solution = solution.copy()  # Hacer copia para preservar
            return
        
        # CALCULAR UPPER BOUND para esta rama
        ub = upper_bound(index, current_weight, current_value)
        
        # PODA INTELIGENTE: Si el upper bound no mejora la mejor solución, 
        # no vale la pena explorar esta rama
        if ub <= best_value:
            return  # PODAR - ahorrar tiempo evitando exploración inútil
        
        # OPCIÓN 1: Incluir el objeto actual (si cabe en la mochila)
        if current_weight + weights[index] <= capacity:
            solution[index] = 1  # Incluir objeto en la solución
            # Llamada recursiva con peso y valor actualizados
            branch_and_bound(index + 1, 
                           current_weight + weights[index],  # Nuevo peso total
                           current_value + values[index],    # Nuevo valor total
                           solution)
            solution[index] = 0  # Limpiar para la siguiente opción
        
        # OPCIÓN 2: No incluir el objeto actual
        # Siempre exploramos esta opción (a menos que hayamos podado)
        branch_and_bound(index + 1, current_weight, current_value, solution)
    
    # Variables globales para mantener la mejor solución encontrada
    best_value = 0  # Mejor valor encontrado hasta ahora
    best_solution = [0] * len(weights)  # Mejor combinación de objetos
    solution = [0] * len(weights)  # Solución temporal para la búsqueda
    
    # Comenzar la búsqueda desde el primer objeto
    branch_and_bound(0, 0, 0, solution)
    return best_value, best_solution
```

---

## 7. ALGORITMOS GREEDY

### Concepto Fundamental

Hacer la elección localmente óptima en cada paso, esperando llegar al óptimo global.

### Características:

- **Ventajas:** Rápidos, simples
- **Desventajas:** No siempre dan solución óptima
- **Aplicable:** Cuando problema tiene propiedad greedy

### Problema: Coin Change Greedy

```ini
DIAGRAMA ASCII:
Cantidad: 67
Monedas: [50, 20, 10, 5, 1]

67 → usar 50 → queda 17
17 → usar 10 → queda 7
7  → usar 5  → queda 2
2  → usar 1  → queda 1
1  → usar 1  → queda 0

Solución: [1, 0, 1, 1, 2] (1×50, 1×10, 1×5, 2×1)
```

**ALGORITMO:**

```python
def coin_change_greedy(coins, amount):
    """
    Resuelve el problema de cambio de monedas usando algoritmo greedy
    
    ¿Qué es un algoritmo greedy?
    En cada paso, toma la decisión que parece mejor EN ESE MOMENTO,
    sin considerar las consecuencias futuras.
    
    Estrategia greedy para monedas:
    Siempre usar la moneda más grande posible primero.
    
    ¿Por qué funciona para algunos sistemas de monedas?
    Para monedas como [1,5,10,25] (sistema estadounidense), esta
    estrategia greedy da la solución óptima. Pero no siempre funciona.
    
    Ejemplo: amount=67, coins=[50,20,10,5,1]
    - Usar 1×50 → queda 17
    - Usar 1×10 → queda 7  
    - Usar 1×5  → queda 2
    - Usar 2×1  → queda 0
    Total: 5 monedas
    """
    # PASO 1: Ordenar monedas de mayor a menor (estrategia greedy)
    coins.sort(reverse=True)
    
    result = []  # Lista para contar cuántas monedas de cada tipo usamos
    
    # PASO 2: Para cada tipo de moneda (empezando por la más grande)
    for coin in coins:
        # DECISIÓN GREEDY: Usar tantas monedas de este tipo como sea posible
        count = amount // coin  # División entera = número máximo de esta moneda
        
        # Ejemplo: si amount=67 y coin=50, entonces count = 67//50 = 1
        result.append(count)    # Guardar cuántas monedas de este tipo usamos
        
        # Actualizar el amount restante
        amount -= count * coin  # Restar el valor total de las monedas usadas
        
        # Ejemplo: amount = 67 - (1×50) = 17
    
    # VERIFICAR: ¿Logramos hacer el cambio exacto?
    # Si amount = 0, significa que pudimos dar cambio exacto
    # Si amount > 0, significa que no hay solución exacta con estas monedas
    return result if amount == 0 else None
```

---

## 8. ÁRBOLES DE HUFFMAN

### Concepto Fundamental

Codificación de caracteres usando frecuencias para minimizar longitud total.

### Construcción del Árbol:

```f90
DIAGRAMA ASCII - Construcción:
Frecuencias: A:5, B:9, C:12, D:13, E:16, F:45

Paso 1: Crear nodos hoja
   A(5) B(9) C(12) D(13) E(16) F(45)

Paso 2: Combinar dos menores
     14
    / \
  A(5) B(9)

Paso 3: Continuar...
     25
    /  \
  14    C(12)
 / \
A(5) B(9)

Resultado final:
      100
     /    \
   55      F(45)
  /  \
 25   E(16) D(13)
/ \
14  C(12)
/\
A B
```

**ALGORITMO:**

```python
from queue import PriorityQueue

class Node:
    """
    Clase para representar nodos del árbol de Huffman
    
    ¿Qué información necesita cada nodo?
    - char: el carácter (None para nodos internos)
    - freq: frecuencia/probabilidad del carácter  
    - left/right: referencias a hijos izquierdo y derecho
    """
    def __init__(self, char, freq):
        self.char = char    # Carácter (None para nodos internos del árbol)
        self.freq = freq    # Frecuencia de aparición del carácter
        self.left = None    # Hijo izquierdo (para código binario '0')
        self.right = None   # Hijo derecho (para código binario '1')
    
    def __lt__(self, other):
        """
        Método especial para comparar nodos
        Necesario para que PriorityQueue pueda ordenar los nodos por frecuencia
        """
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    """
    Construye el árbol de Huffman a partir de las frecuencias de caracteres
    
    ¿Cómo funciona el algoritmo de Huffman?
    1. Crear un nodo hoja para cada carácter
    2. Repetir hasta que quede solo un nodo:
       - Tomar los dos nodos con menor frecuencia
       - Crear un nuevo nodo padre que los combine
       - La frecuencia del padre = suma de frecuencias de los hijos
    3. El último nodo es la raíz del árbol
    
    ¿Por qué usar PriorityQueue?
    Nos permite tomar siempre los dos nodos con menor frecuencia
    de manera eficiente (O(log n) por extracción).
    """
    # Cola de prioridad: siempre nos dará el nodo con menor frecuencia primero
    pq = PriorityQueue()
    
    # PASO 1: Crear nodos hoja para cada carácter
    for char, freq in frequencies.items():
        # Cada carácter se convierte en un nodo hoja
        pq.put(Node(char, freq))
    
    # PASO 2: Construir árbol combinando nodos de menor frecuencia
    while pq.qsize() > 1:  # Mientras haya más de un nodo
        
        # Tomar los dos nodos con menor frecuencia
        left = pq.get()   # Nodo con menor frecuencia
        right = pq.get()  # Nodo con segunda menor frecuencia
        
        # Crear nodo padre que combine a estos dos nodos
        merged = Node(None, left.freq + right.freq)  # char=None (nodo interno)
        merged.left = left    # Hijo izquierdo
        merged.right = right  # Hijo derecho
        
        # Agregar el nodo combinado de vuelta a la cola
        # Este nuevo nodo compite con otros nodos para ser el siguiente más pequeño
        pq.put(merged)
    
    # El último nodo en la cola es la raíz del árbol completo
    return pq.get()

def generate_codes(root):
    """
    Genera los códigos binarios para cada carácter basándose en el árbol
    
    ¿Cómo se generan los códigos?
    - Recorremos el árbol desde la raíz hasta cada hoja
    - Cada vez que vamos a la izquierda, agregamos '0' al código
    - Cada vez que vamos a la derecha, agregamos '1' al código
    - Cuando llegamos a una hoja, tenemos el código completo para ese carácter
    
    Ejemplo:
          ROOT
         /    \
        A      B
    Código A = '0', Código B = '1'
    """
    if not root:
        return {}
    
    codes = {}  # Diccionario: carácter -> código binario (string)
    
    def dfs(node, code):
        """
        Búsqueda en profundidad (DFS) para generar códigos
        
        node: nodo actual del árbol
        code: código binario acumulado hasta este nodo
        """
        if node.char:  # Si es nodo hoja (tiene carácter)
            # Guardar el código para este carácter
            codes[node.char] = code
        else:
            # Si es nodo interno, continuar la búsqueda en ambos hijos
            dfs(node.left, code + '0')   # Izquierda = agregar '0'
            dfs(node.right, code + '1')  # Derecha = agregar '1'
    
    # Comenzar DFS desde la raíz con código vacío
    dfs(root, '')
    return codes
```

**Códigos resultantes:**

- F: "0"
- C: "100"
- D: "101"
- A: "1100"
- B: "1101"
- E: "111"

---

## 9. SUFFIX TRIE

### Concepto Fundamental

Estructura de datos que almacena todos los sufijos de una cadena para búsquedas rápidas.

### Construcción:

```sh
DIAGRAMA ASCII - Suffix Trie para "BANANA":
Sufijos: BANANA, ANANA, NANA, ANA, NA, A

      ROOT
     /  |  \
    B   A   N
    |   |   |
    A   N   A
    |   |   |
    N   A   N
    |   |   |
    A   N   A
    |   |   |
    N   A   $
    |   |
    A   $
    |
    $

$ representa final de cadena
```

**ALGORITMO:**

```python
class TrieNode:
    """
    Clase para representar cada nodo del Suffix Trie
    
    ¿Qué información guarda cada nodo?
    - char: el carácter que representa
    - indices: lista de posiciones donde aparece este sufijo en el texto original
    - is_final: ¿es el final de un sufijo completo?
    - children: lista de nodos hijos
    """
    def __init__(self, char, is_final=False):
        self.char = char            # Carácter que representa este nodo
        self.indices = []           # Posiciones donde aparece este sufijo
        self.is_final = is_final    # ¿Es el final de un sufijo completo?
        self.children = []          # Lista de nodos hijos

class SuffixTrie:
    """
    Estructura de datos Suffix Trie
    
    ¿Qué es un Suffix Trie?
    Es un árbol que almacena TODOS los sufijos de una cadena.
    
    Ejemplo para "ABC":
    Sufijos: "ABC", "BC", "C"
    
    ¿Para qué sirve?
    - Buscar patrones muy rápido: O(longitud_patrón)
    - Encontrar subcadenas repetidas
    - Análisis de texto y ADN
    """
    
    def __init__(self):
        # Crear nodo raíz con carácter especial '#'
        self.root = TrieNode('#', False)
    
    def insert_suffix(self, suffix, start_index):
        """
        Inserta un sufijo específico en el trie
        
        Parámetros:
        - suffix: el sufijo a insertar (ej: "ANA" de "BANANA")
        - start_index: posición donde inicia este sufijo en el texto original
        
        ¿Cómo funciona?
        Recorre carácter por carácter del sufijo. Si un carácter ya existe
        en el trie, lo reutiliza. Si no existe, crea un nuevo nodo.
        """
        current = self.root  # Empezamos desde la raíz
        
        # Recorrer cada carácter del sufijo
        for i, char in enumerate(suffix):
            found = False
            
            # Buscar si ya existe un hijo con este carácter
            for child in current.children:
                if child.char == char:
                    # El carácter ya existe, reutilizar el nodo
                    child.indices.append(start_index + i)  # Agregar posición
                    current = child  # Moverse a este nodo hijo
                    found = True
                    break
            
            if not found:
                # El carácter no existe, crear nuevo nodo
                is_last_char = (i == len(suffix) - 1)  # ¿Es el último carácter?
                new_node = TrieNode(char, is_last_char)
                new_node.indices.append(start_index + i)
                current.children.append(new_node)  # Agregarlo como hijo
                current = new_node  # Moverse al nuevo nodo
    
    def build_from_string(self, text):
        """
        Construye el trie completo insertando TODOS los sufijos de la cadena
        
        ¿Qué hace exactamente?
        Para una cadena como "BANANA", inserta los sufijos:
        - "BANANA" (comienza en posición 0)
        - "ANANA"  (comienza en posición 1) 
        - "NANA"   (comienza en posición 2)
        - "ANA"    (comienza en posición 3)
        - "NA"     (comienza en posición 4)
        - "A"      (comienza en posición 5)
        """
        # Para cada posición posible en el texto
        for i in range(len(text)):
            # Insertar el sufijo que comienza en la posición i
            self.insert_suffix(text[i:], i)
    
    def search_pattern(self, pattern):
        """
        Busca un patrón en el trie (¡muy rápido!)
        
        ¿Cómo funciona la búsqueda?
        Sigue el camino del patrón en el trie carácter por carácter.
        Si en algún punto no existe el carácter, el patrón no está.
        Si llega al final, retorna todas las posiciones donde aparece.
        
        Complejidad: O(longitud_del_patrón) - ¡súper rápido!
        
        Retorna: Lista de posiciones donde aparece el patrón
        """
        current = self.root
        
        # Seguir el camino del patrón en el trie
        for char in pattern:
            found = False
            
            # Buscar el carácter entre los hijos del nodo actual
            for child in current.children:
                if child.char == char:
                    current = child  # Avanzar a este nodo hijo
                    found = True
                    break
            
            if not found:
                # El carácter no existe en el trie
                return []  # Patrón no encontrado
        
        # Si llegamos aquí, el patrón existe en el trie
        # Las posiciones están guardadas en el nodo final
        return current.indices
```

### Aplicaciones:

- Búsqueda de patrones: O(m) donde m = longitud del patrón
- Encontrar subcadenas más largas repetidas
- Análisis de ADN y proteínas

---

## 10. PROBLEMAS CLÁSICOS

### A. Ordenamiento Topológico

**Problema:** Ordenar elementos respetando dependencias.

```ini
DIAGRAMA ASCII:
Grafo: A→B, A→C, B→D, C→D

A ----→ B
|       |
|       ↓
↓       D
C ------↗

Orden posible: A, B, C, D o A, C, B, D
```

**Algoritmo (DFS):**

```python
def topological_sort(graph):
    visited = set()        # Nodos completamente procesados
    temp_visited = set()   # Nodos en proceso (para detectar ciclos)
    result = []           # Lista resultado del ordenamiento
    
    def dfs(node):
        # Si el nodo está en proceso, hay un ciclo
        if node in temp_visited:
            return False  # Ciclo detectado
        
        # Si ya fue visitado completamente, no hacer nada
        if node in visited:
            return True
        
        # Marcar nodo como "en proceso"
        temp_visited.add(node)
        
        # Visitar recursivamente todos los vecinos (dependencias)
        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False  # Propagar detección de ciclo
        
        # Terminar procesamiento del nodo
        temp_visited.remove(node)  # Ya no está en proceso
        visited.add(node)          # Marcarlo como completamente visitado
        result.append(node)        # Agregarlo al resultado
        return True
    
    # Procesar todos los nodos del grafo
    for node in graph:
        if node not in visited:
            if not dfs(node):
                return None  # El grafo tiene ciclos, no hay orden topológico
    
    # El DFS agrega nodos al final, así que invertimos para orden correcto
    return result[::-1]  # Reversar para obtener orden topológico
```

### B. Problema de la Moneda Falsa

**Problema:** Encontrar moneda con peso diferente usando balanza.

```ini
DIAGRAMA ASCII:
12 monedas, 1 falsa (más liviana)

Pesada 1: [1,2,3,4] vs [5,6,7,8]
   - Si equilibrio → falsa en {9,10,11,12}
   - Si izq. < der. → falsa en {1,2,3,4}
   - Si izq. > der. → falsa en {5,6,7,8}

Pesada 2: Dividir grupo sospechoso en 3
Pesada 3: Identificar la falsa
```

---

## RESUMEN DE COMPLEJIDADES

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso | Espacio |
|-----------|------------|---------------|-----------|---------|
| Fuerza Bruta | O(n²) | O(n²) | O(n²) | O(1) |
| Decrease & Conquer | O(log n) | O(log n) | O(log n) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| DP - Coin Change | O(n*k) | O(n*k) | O(n*k) | O(n*k) |
| Backtracking | O(n!) | O(2^n) | O(2^n) | O(n) |
| Branch & Bound | O(1) | O(2^n) | O(2^n) | O(n) |
| Huffman | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Suffix Trie | O(n²) | O(n²) | O(n²) | O(n²) |

---

## EJERCICIOS DE PRÁCTICA

### 1. Implementa Closest Pair con Divide y Vencerás

**Pista:** Dividir puntos por coordenada x, encontrar mínimo en cada mitad, verificar banda central.

### 2. Resuelve N-Queens con Backtracking

**Pista:** Colocar reinas fila por fila, verificar ataques diagonales y verticales.

### 3. Implementa Knapsack 0/1 con DP

**Pista:** T[i][w] = máximo valor con primeros i objetos y peso máximo w.

### 4. Construye Suffix Array para cadena dada

**Pista:** Array de índices de sufijos ordenados lexicográficamente.

### 5. Algoritmo Greedy para Job Scheduling

**Pista:** Ordenar trabajos por tiempo de finalización.

---

## CONSEJOS PARA EL EXAMEN

### 📝 **Estrategias de Resolución:**

1. **Identifica el tipo de problema:**

   - ¿Necesitas explorar todas las posibilidades? → Fuerza Bruta/Backtracking
   - ¿Hay subproblemas superpuestos? → Programación Dinámica
   - ¿Puedes dividir en partes iguales? → Divide y Vencerás
   - ¿La elección greedy funciona? → Algoritmos Greedy

2. **Analiza la complejidad requerida:**

   - O(n²) → Probablemente fuerza bruta o DP simple
   - O(n log n) → Divide y vencerás o estructuras de datos eficientes
   - O(2^n) → Backtracking o branch and bound

3. **Verifica casos especiales:**

   - Casos base en recursión
   - Arrays vacíos
   - Un solo elemento

### 🎯 **Patrones Comunes:**

- **Optimización:** DP, Greedy, Branch & Bound
- **Búsqueda completa:** Backtracking, Fuerza Bruta
- **División del problema:** Divide y Vencerás, Decrease & Conquer
- **Estructuras de cadenas:** Tries, Suffix Trees, KMP

### ⚡ **Implementación Rápida:**

- Practica escribir a mano los algoritmos básicos
- Memoriza las estructuras de datos fundamentales
- Conoce las complejidades de memoria y tiempo

---

**¡ÉXITO EN TU EXAMEN! 🚀**

Esta guía cubre todos los conceptos fundamentales. Practica implementando cada algoritmo y resolviendo problemas similares para dominar los algoritmos avanzados.