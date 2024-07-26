import networkx as nt
import matplotlib.pyplot as mt

# Grafo desde un archivo .txt
def grafo_archivo(ruta_archivo):
    grafo = nt.Graph()
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminar espacios en blanco
            linea = linea.strip()
            # Separar los atributos por ','
            parts = linea.split(',')
            # Guardar los atribulos en variables
            u = parts[0]
            v = parts[1]
            weight = int(parts[2])
            # Añadir arista al grafo
            grafo.add_edge(u, v, weight=weight)
    return grafo

ruta = r'"C:\Users\Usuario iTC\Downloads\Grafo_no_dirigido.txt"'
g = grafo_archivo(ruta)

# Función para crear un diccionario por si los indices son cadenas
def crear_indices(graph):
    indices = {}
    for i, nodo in enumerate(graph.nodes):
        indices[nodo] = i
    return indices

# Creación de diccionario de indices, por si los nodos son cadenas
indices = crear_indices(g)

# Función de Kruskal
def kruskal(grafo):
    # Grafo vacio que almacenará el Árbol de Recubrimiento Mínimo
    arm = nt.Graph()
    # Oredenar las aristas por su peso
    aristas = sorted(grafo.edges(data=True), key=lambda x: x[2]['weight'])
    # Creación de los conjuntos individuales por cada nodo
    conjunto = [i for i in range(len(grafo.nodes))]

    for arista in aristas:
        n1, n2, peso = arista
        # Con las siguientes líneas de código hacemos que las letras sean indices en una lista
        compu = buscar(conjunto, indices[n1])
        compv = buscar(conjunto, indices[n2])

        if compu != compv:
            fusionar(conjunto, indices[n1], indices[n2])
            arm.add_edge(n1, n2, weight = arista[2]['weight'])

    return arm

# Función para encontrar el conjunto en el que se encuentra un nodo
def buscar(conjunto, i):
    if conjunto[i] == i:
        return i
    else:
        return buscar(conjunto, conjunto[i])

# Fucnión para unir los conjuntos
def fusionar(conjunto, u, v):
    conjunto[buscar(conjunto, u)] = buscar(conjunto, v)

#Imprimir Grafos
for (u, v, p) in g.edges.data('weight'):
    print(f"({u}, {v}, {p})")

print()

arm = kruskal(g)
for (u, v, p) in arm.edges.data('weight'):
    print(f"({u}, {v}, {p})")

# Guardar Árbol de Recubrimiento Mínimo en un archivo
ruta_destino = r'C:\Users\Usuario iTC\Desktop\Yo\UTPL\Analisis de Algoritmos\graf_kruskal.txt'
def guardar_grafo_archivo(arm, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")

guardar_grafo_archivo(arm, ruta_destino)

