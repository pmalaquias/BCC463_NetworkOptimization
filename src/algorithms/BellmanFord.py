
from algorithms.graph import Graph


def BellmanFord(graph: Graph, origem: int):
    # Inicialização dos conjuntos e vetores
    dt = {v: float('inf') for v in range(graph.n + 1)}  # Vetor de distâncias mínimas
    rot = {v: None for v in range(graph.n + 1)}  # Vetor de rotas (vértices anteriores)

    # Definir a distância de origem como 0
    dt[origem] = 0

    # Relaxação das arestas
    for _ in range(graph.n - 1):
        for (u, v), peso in graph.capacity.items():
            if dt[u] + peso < dt[v]:
                dt[v] = dt[u] + peso
                rot[v] = u

    # Verificação de ciclos negativos
    for (u, v), peso in graph.capacity.items():
        if dt[u] + peso < dt[v]:
            print("O grafo contém um ciclo negativo.")
            return None, None, True
    # for u in graph.adj:
    #     for v in graph.adj[u]:
    #         peso = graph.capacity.get((u, v), float('inf'))
    #         if dt[u] + peso < dt[v]:  # Se ainda houver relaxamento, há um ciclo negativo
    #             raise ValueError("O grafo contém um ciclo negativo.")

    return dt, rot, False