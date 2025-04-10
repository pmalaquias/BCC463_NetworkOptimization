from collections import deque


def Dinitz(flow):
    """
    Algoritmo de Dinitz para Fluxo Máximo.
    Esta função implementa o algoritmo de Dinitz para calcular o fluxo máximo em uma rede de fluxo.
    O algoritmo utiliza uma abordagem de rede em camadas com BFS para construir grafos de nível e DFS 
    para encontrar caminhos aumentantes.
    Argumentos:
        flow: Um objeto que representa a rede de fluxo. Ele deve ter os seguintes atributos:
            - n: O número de nós na rede.
            - source: O nó de origem (inteiro).
            - sink: O nó de destino (inteiro).
            - graph: Um objeto com uma lista de adjacência `adj` representando a estrutura do grafo.
            - capacity: Uma lista 2D onde capacity[u][v] representa a capacidade da aresta u → v.
            - flow: Uma lista 2D onde flow[u][v] representa o fluxo atual na aresta u → v.
    Retorna:
        int: O fluxo máximo da origem ao destino na rede de fluxo fornecida.
    Notas:
        - O algoritmo constrói um grafo de nível usando BFS para determinar o caminho mais curto 
        (em termos de arestas) da origem ao destino.
        - Em seguida, utiliza DFS para enviar fluxo ao longo desses caminhos, respeitando as restrições de capacidade.
        - O processo se repete até que não seja possível encontrar mais caminhos aumentantes no grafo de nível.
    """
    n = flow.n
    s = flow.source
    t = flow.sink
    max_flow = 0

    #  BFS para construir rede em camadas
    def build_level_graph():
        level = [-1] * (n + 1)
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in flow.graph.adj[u]:
                if level[v] == -1 and flow.capacity[u][v] - flow.flow[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level

    #  DFS para encontrar caminhos aumentantes
    def send_flow(u, flow_amt, level, next_edge):
        if u == t:
            return flow_amt
        for i in range(next_edge[u], len(flow.graph.adj[u])):
            v = flow.graph.adj[u][i]
            if level[v] == level[u] + 1 and flow.capacity[u][v] - flow.flow[u][v] > 0:
                pushed = send_flow(v, min(flow_amt, flow.capacity[u][v] - flow.flow[u][v]), level, next_edge)
                if pushed > 0:
                    flow.flow[u][v] += pushed
                    flow.flow[v][u] -= pushed
                    return pushed
            next_edge[u] += 1
        return 0

    #  Loop principal de Dinitz
    while True:
        level = build_level_graph()
        if level[t] == -1:
            break  # sem caminho s → t
        next_edge = [0] * (n + 1)
        while True:
            pushed = send_flow(s, float('inf'), level, next_edge)
            if pushed == 0:
                break
            max_flow += pushed

    return max_flow
