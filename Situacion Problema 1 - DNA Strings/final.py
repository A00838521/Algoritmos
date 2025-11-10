def z_algoritmo(patron, texto):
    """
    Implementa el algoritmo Z-Array para búsqueda de patrones en tiempo O(n+m).
    Retorna todas las posiciones donde aparece el patrón en el texto.
    """
    concat = patron + "$" + texto
    n = len(concat)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and concat[z[i]] == concat[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    posiciones = []
    patron_len = len(patron)
    for i in range(patron_len + 1, n):
        if z[i] == patron_len:
            posiciones.append(i - patron_len - 1)
    
    return posiciones

def cargar_genoma_simple(archivo):
    """Carga secuencia genómica desde archivo FASTA."""
    with open(archivo, 'r') as f:
        contenido = f.read()
        lineas = contenido.strip().split('\n')
        return ''.join(lineas[1:])

def cargar_proteinas_simple(archivo):
    """Carga secuencias de proteínas desde archivo FASTA."""
    proteinas = {}
    nombre_actual = None
    secuencia_actual = ""
    
    with open(archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea.startswith('>'):
                if nombre_actual:
                    proteinas[nombre_actual] = secuencia_actual
                nombre_actual = linea[1:]
                secuencia_actual = ""
            else:
                secuencia_actual += linea
        
        if nombre_actual:
            proteinas[nombre_actual] = secuencia_actual
    
    return proteinas

TABLA_CODONES = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M", "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K", "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L", "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q", "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V", "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E", "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S", "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*", "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W"
}

def traducir_simple(adn, inicio=0):
    """Traduce secuencia de ADN a proteína desde posición específica."""
    proteina = ""
    for i in range(inicio, len(adn) - 2, 3):
        codon = adn[i:i+3]
        aa = TABLA_CODONES.get(codon, "X")
        proteina += aa
    
    return proteina

def buscar_proteina_simple(genoma, proteina_objetivo, nombre, usar_slippery=False):
    """
    Busca proteína en los tres marcos de lectura usando Z-Algorithm.
    Opcionalmente aplica detección de slippery sequences.
    """
    for frame in range(3):
        proteina_genoma = traducir_simple(genoma, frame)
        posiciones = z_algoritmo(proteina_objetivo, proteina_genoma)
        
        if posiciones:
            posicion = posiciones[0]
            inicio_nt = frame + (posicion * 3)
            fin_nt = inicio_nt + (len(proteina_objetivo) * 3)
            
            print(f"{nombre}: Frame {frame}, posición {inicio_nt}-{fin_nt}")
            
            return {
                'encontrada': True,
                'frame': frame,
                'inicio': inicio_nt,
                'fin': fin_nt,
                'tipo': 'exacta'
            }
    
    if usar_slippery:
        return buscar_con_slippery_sequence(genoma, proteina_objetivo, nombre)
    
    print(f"{nombre}: No encontrada")
    return {'encontrada': False}

def buscar_con_slippery_sequence(genoma, proteina_objetivo, nombre):
    """
    Detecta proteínas mediante análisis de slippery sequences.
    Busca patrón TTTAAAC y analiza regiones circundantes.
    """
    patron_tttaaac = "TTTAAAC"
    posiciones_patron = []
    
    for i in range(len(genoma) - len(patron_tttaaac) + 1):
        if genoma[i:i+len(patron_tttaaac)] == patron_tttaaac:
            posiciones_patron.append(i)
    
    if not posiciones_patron:
        return {'encontrada': False}
    
    for pos_patron in posiciones_patron:
        inicio_region = max(0, pos_patron - 1000)
        fin_region = min(len(genoma), pos_patron + 1000)
        longitud_min_fragmento = 15
        
        for inicio_fragmento in range(0, len(proteina_objetivo) - longitud_min_fragmento + 1, 5):
            for fin_fragmento in range(inicio_fragmento + longitud_min_fragmento, len(proteina_objetivo) + 1, 5):
                fragmento = proteina_objetivo[inicio_fragmento:fin_fragmento]
                
                for frame in range(3):
                    if inicio_region + frame < len(genoma):
                        region_genoma = genoma[inicio_region + frame:fin_region]
                        proteina_region = traducir_simple(region_genoma)
                        
                        posiciones_frag = z_algoritmo(fragmento, proteina_region)
                        
                        if posiciones_frag:
                            pos_abs = inicio_region + frame + (posiciones_frag[0] * 3)
                            distancia_al_patron = abs(pos_abs - pos_patron)
                            
                            if distancia_al_patron < 100:
                                inicio_estimado = pos_abs - (inicio_fragmento * 3)
                                fin_estimado = inicio_estimado + (len(proteina_objetivo) * 3)
                                
                                if inicio_estimado >= 0 and fin_estimado <= len(genoma):
                                    print(f"{nombre}: Frame {frame}, posición {inicio_estimado}-{fin_estimado} (slippery)")
                                    
                                    return {
                                        'encontrada': True,
                                        'frame': frame,
                                        'inicio': inicio_estimado,
                                        'fin': fin_estimado,
                                        'tipo': 'slippery_sequence'
                                    }
    
    return {'encontrada': False}

print("Cargando archivos...")
genoma_wuhan = cargar_genoma_simple('SARS-COV-2-MN908947.3.txt')
proteinas = cargar_proteinas_simple('seq-proteins.txt')

print(f"Genoma cargado: {len(genoma_wuhan):,} nucleótidos")
print(f"Proteínas cargadas: {len(proteinas)}")

def analizar_todas_las_proteinas():
    """Ejecuta análisis completo de proteínas en los tres marcos de lectura."""
    print("Analizando proteínas SARS-CoV-2...")
    
    resultados = {}
    proteinas_encontradas = 0
    
    for nombre, secuencia in proteinas.items():
        usar_slippery = (nombre == 'QHD43415_11')
        resultado = buscar_proteina_simple(genoma_wuhan, secuencia, nombre, usar_slippery)
        
        resultados[nombre] = resultado
        if resultado['encontrada']:
            proteinas_encontradas += 1
    
    print(f"\nResultados: {proteinas_encontradas}/{len(proteinas)} proteínas encontradas")

analizar_todas_las_proteinas()

def traducir_codon_simple(codon):
    """Traduce codón individual usando tabla global de codones."""
    return TABLA_CODONES.get(codon, "X") if len(codon) == 3 else "X"

def comparar_genomas_simple(genoma_wuhan, genoma_texas):
    """
    Compara secuencias genómicas e identifica diferencias nucleotídicas.
    Retorna lista de diferencias con posiciones y cambios.
    """
    len_wuhan = len(genoma_wuhan)
    len_texas = len(genoma_texas)
    min_len = min(len_wuhan, len_texas)
    
    diferencias = []
    for i in range(min_len):
        if genoma_wuhan[i] != genoma_texas[i]:
            diferencias.append({
                'posicion': i,
                'wuhan': genoma_wuhan[i],
                'texas': genoma_texas[i]
            })
    
    identidad = ((min_len - len(diferencias)) / min_len * 100)
    print(f"Comparación genómica: {len(diferencias)} diferencias, identidad {identidad:.2f}%")
    
    return diferencias

def analizar_codones_afectados(diferencias, genoma_wuhan, genoma_texas):
    """
    Analiza impacto de diferencias nucleotídicas en codones y aminoácidos.
    Determina cambios en la traducción de proteínas.
    """
    print("Diferencias en codones y aminoácidos:")
    
    for diff in diferencias:
        pos = diff['posicion']
        nt_wuhan = diff['wuhan']
        nt_texas = diff['texas']
        
        codon_inicio = (pos // 3) * 3
        
        if codon_inicio + 2 < len(genoma_wuhan) and codon_inicio + 2 < len(genoma_texas):
            codon_wuhan = genoma_wuhan[codon_inicio:codon_inicio + 3]
            codon_texas = genoma_texas[codon_inicio:codon_inicio + 3]
            
            aa_wuhan = traducir_codon_simple(codon_wuhan)
            aa_texas = traducir_codon_simple(codon_texas)
            
            print(f"Posición {pos:,}: {nt_wuhan}→{nt_texas}, {codon_wuhan}({aa_wuhan}) → {codon_texas}({aa_texas})")

print("Cargando genoma de Texas...")
genoma_texas = cargar_genoma_simple('SARS-COV-2-MT106054.1.txt')

diferencias_genomicas = comparar_genomas_simple(genoma_wuhan, genoma_texas)
analizar_codones_afectados(diferencias_genomicas, genoma_wuhan, genoma_texas)