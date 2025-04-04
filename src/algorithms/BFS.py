from collections import deque

from algorithms.graph import Graph


def BFS(graph: Graph, v: int):
   
    Q = deque()  # Criando a fila Q
    visited = [False] * (graph.n + 1)  # Lista de visitados
    result = []  # Lista de resultados

    visited[v] = True  # Marcando o vértice inicial como visitado
    Q.append(v)  # Adicionando o vértice inicial à fila

    while Q:  # Enquanto a fila não estiver vazia
        curr = Q.popleft() # Retirando o primeiro elemento da fila
        result.append(curr) # Adicionando o vértice atual ao resultado

        for w in graph.adj[curr]:
            if not visited[w]:
                visited[w] = True
                Q.append(w)
    
    print(" ".join(map(str, result)))
    return result
