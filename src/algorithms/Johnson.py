
from algorithms.BellmanFord import BellmanFord
from algorithms.Dijkstra import Dijkstra
from algorithms.graph import Graph


def johnson(graph: Graph):
    # Passo 1: Adiciona novo vértice q = 0
    q = 0
    novo_grafo = Graph(graph.n + 1, directed=True)
    
    # Copia todas as arestas do grafo original
    for (u, v), w in graph.capacity.items():
        novo_grafo.add_edge(u, v, w)
    
    # Conecta q a todos os vértices com peso 0
    for v in range(1, graph.n + 1):
        novo_grafo.add_edge(q, v, 0)

    # Passo 2: Bellman-Ford a partir do novo vértice q
    h, predecessors_bf, has_negative_cycle= BellmanFord(novo_grafo, q)

    # Se houve ciclo negativo, retorna None
    if has_negative_cycle:
        print("O grafo contém ciclo negativo!")
        return None

    # Passo 3: Recalcular pesos das arestas
    reweighted_graph = Graph(graph.n, directed=True)
    for (u, v), w in graph.capacity.items():
        w_prime = w + h[u] - h[v]
        reweighted_graph.add_edge(u, v, w_prime)

    # Passo 4: Rodar Dijkstra de cada vértice
    matriz = [[float('inf')] * graph.n for _ in range(graph.n)]

    for u in range(1, graph.n + 1):
        dist, _ = Dijkstra(reweighted_graph, u)
        for v in range(1, graph.n + 1):
            if dist[v] != float('inf'):
                matriz[u - 1][v - 1] = dist[v] - h[u] + h[v]
            elif u == v:
                matriz[u - 1][v - 1] = 0

    return matriz