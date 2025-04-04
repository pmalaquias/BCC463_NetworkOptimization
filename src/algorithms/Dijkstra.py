
import heapq  # fila de prioridade

from algorithms.graph import Graph  # importa a classe grafo


def Dijkstra (graph: Graph, origem: int):

    #inicialização dos conjuntos e vetores
    F = set() #conjunto de vértices fechados
    A = set(range(graph.n +1)) #conjunto de vértices abertos
    dt = {v: float('inf') for v in A} #vetor de distâncias mínimas
    rot = {v: None for v in A} #vetor de rotas (vértices anteriores)

    #DT inicial e rot
    # print(f"Origem: {origem}")
    # print("dt: ", dt)
    # print("rot: ", rot)
    

    #Definir a distância de origem como 0 e inserir na fila de prioridade
    dt[origem] = 0
    fila_prioridade = [(0, origem)]

    while A:
        #Escolher o vértice em A com a menor distancia em dt (o mais próximo)
        while fila_prioridade:
            d, v = heapq.heappop(fila_prioridade)
            if v in A:
                break
        
        else:
            break

        #Remover v de A e inserir em F
        A.remove(v)
        F.add(v)

        #N: Distância de vizinho abertos de V
        N = set(graph.adj[v]) & A

        # Atualizar distâncias dos Vizinhos
        for viz in N:
            peso = graph.capacity.get((v, viz), float('inf'))  # Obtém o peso da aresta
            nova_dist = dt[v] + peso
            if nova_dist < dt[viz]:  # Relaxamento
                dt[viz] = nova_dist
                rot[viz] = v
                heapq.heappush(fila_prioridade, (nova_dist, viz))

    return dt, rot
