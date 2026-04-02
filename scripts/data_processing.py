import pandas as pd
from itertools import combinations
from collections import Counter

print("Cargando datos minimizados...")
df = pd.read_csv('metadata.csv.zip', usecols=['authors'], nrows=1000)
df = df.dropna(subset=['authors'])

edges_list = []
nodes_set = set()

print("Procesando autores y conexiones...")
for authors_str in df['authors']:
    authors = [author.strip() for author in authors_str.split(';')]
    authors = [a for a in authors if a]
    
    # Filtro de minimización: ignorar papers con más de 10 autores
    if 1 < len(authors) <= 10:
        nodes_set.update(authors)
        for pair in combinations(sorted(authors), 2):
            edges_list.append(pair)

edges_counted = Counter(edges_list)

print("Generando archivos para Gephi...")
df_nodes = pd.DataFrame({'Id': list(nodes_set), 'Label': list(nodes_set)})

edges_data = []
for (source, target), weight in edges_counted.items():
    edges_data.append({
        'Source': source, 
        'Target': target, 
        'Type': 'Undirected', 
        'Weight': weight
    })
    
df_edges = pd.DataFrame(edges_data)

df_nodes.to_csv('nodos_reducidos.csv', index=False)
df_edges.to_csv('aristas_reducidas.csv', index=False)

print(f"¡Listo! Se han generado {len(df_nodes)} nodos y {len(df_edges)} aristas.")