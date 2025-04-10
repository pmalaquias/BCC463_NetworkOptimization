
from algorithms.bellman_ford import BellmanFord
from algorithms.dijkstra import Dijkstra
from algorithms.graph import Graph


def Johnson(graph: Graph):
    """
    Implementa o algoritmo de Johnson para encontrar os caminhos mínimos entre todos os pares de vértices
    em um grafo ponderado e direcionado. Este algoritmo lida com grafos que possuem arestas de peso negativo,
    mas não ciclos de peso negativo.
    Parâmetros:
        graph (Graph): O grafo de entrada representado como uma instância da classe `Graph`. 
                    Deve conter o número de vértices (`n`) e um dicionário de capacidades 
                    de arestas (`capacity`), onde as chaves são tuplas de arestas (u, v) 
                    e os valores são os pesos.
    Retorna:
        list[list[float]]: Uma lista 2D (matriz) onde o elemento na posição [i][j] representa 
                        a distância do caminho mínimo do vértice i+1 ao vértice j+1. Se não 
                        existir caminho, o valor será `float('inf')`. Se o grafo contiver 
                        um ciclo de peso negativo, a função retorna `None`.
    Lança:
        ValueError: Se o grafo de entrada for inválido ou mal formatado.
    Etapas:
        1. Adiciona um novo vértice `q` conectado a todos os outros vértices com arestas de peso 0.
        2. Executa o algoritmo de Bellman-Ford a partir do vértice `q` para detectar ciclos de peso 
        negativo e calcular os valores potenciais (`h`) para reponderar as arestas.
        3. Repondera as arestas do grafo usando os valores potenciais calculados.
        4. Executa o algoritmo de Dijkstra a partir de cada vértice para calcular os caminhos mínimos 
        no grafo reponderado.
        5. Ajusta as distâncias de volta aos pesos originais usando os valores potenciais.
    Notas:
        - O grafo de entrada não deve conter ciclos de peso negativo; caso contrário, o algoritmo 
        terminará precocemente e retornará `None`.
        - Os vértices do grafo são assumidos como indexados a partir de 1.
    """
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