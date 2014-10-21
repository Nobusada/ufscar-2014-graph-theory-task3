# Comandos em python para leitura de um grafo a partir de uma matriz de 
# adjacencia gravada em arquivo texto

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

dataset = 'sgb128'
dataset_dist = '../dataset/' + dataset + '_dist.txt'
dataset_name = '../dataset/' + dataset + '_name.txt'

a = np.loadtxt(dataset_dist)
labels = np.loadtxt(dataset_name, dtype=basestring)

# Obtem as coordenadas em que o peso eh nao-nulo
rows, cols= np.where(a > 0)

# Obtem o peso de cada uma das arestas
weight = [a[rows[i],cols[i]] for i in range(0, len(rows))]

# Cria lista de arestas com e sem peso
edges = zip(rows.tolist(), cols.tolist())
edges_with_weight = zip(rows.tolist(), cols.tolist(), weight)

# Cria um grafo vazio usando NetworkX
g = nx.Graph()

# Insere arestas (cria vertices automaticamente)
# Para inserir os pesos usar um dicionario como parametro adicional
g.add_edges_from(edges)
#g.add_weighted_edges_from(edges_with_weight)

# Linka os nomes com seus respectivos vertices
nomes = dict(zip(g.nodes(), labels.tolist()))

# Mostra vertices e arestas

#print g.nodes()
#print g.edges(data=True)

# Plota resultados em arquivo

pos = nx.circular_layout(g)

nx.draw_networkx_nodes(g, pos, node_size=70)
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_labels(g, pos, nomes, font_size=10)

plt.axis('off')
plt.show()

#plt.figure(1, figsize=(15,15))		# Cria figura para desenhar grafo: 15 eh a dimensao da imagem
#nx.draw_spring(g, node_size=120, font_size=3, edge_width=0.5, alpha=0.5, arrows=False)
#plt.show()
#plt.savefig('arquivo.png')		# Outros formatos: pdf, svg, ...


# OBS: Para leitura de outros formatos ver funcoes
# nx.read_dot, nx.read_edgelist, nx.read_weighted_edgelist, nx.read_gexf, nx.read_gml, nx.read_graphml,...
 
