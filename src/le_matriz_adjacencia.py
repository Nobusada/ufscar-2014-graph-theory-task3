# Comandos em python para leitura de um grafo a partir de uma matriz de 
# adjacência gravada em arquivo texto

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

a = np.loadtxt('USAir97.txt')

# Obtem as coordenadas em que o peso é não-nulo
rows, cols = np.where(a>0)

# Cria lista de arestas
edges = zip(rows.tolist(), cols.tolist())

# Cria um grafo vazio usando NetworkX
g = nx.Graph()

# Insere arestas (cria vértices automaticamente)
# Para inserir os pesos usar um dicionário como parametro adicional
g.add_edges_from(edges)

# Mostra vértices e arestas
g.nodes()
g.edges()

# Plota resultados em arquivo
plt.figure(1, figsize=(15,15))		# Cria figura para desenhar grafo: 15 é a dimensão da imagem
nx.draw_spring(g, node_size=120, font_size=3, edge_width=0.5, alpha=0.5, arrows=False)
plt.savefig('arquivo.png')		# Outros formatos: pdf, svg, ...


# OBS: Para leitura de outros formatos ver funções
# nx.read_dot, nx.read_edgelist, nx.read_weighted_edgelist, nx.read_gexf, nx.read_gml, nx.read_graphml,...
 
