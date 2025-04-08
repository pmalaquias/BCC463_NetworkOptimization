
from algorithms.graph import Graph


class Flow:
    def __init__(self, graph: Graph, source: int, sink: int):
        self.graph = graph
        self.n = graph.n

        self.source = source  # vértice de origem
        self.sink = sink      # vértice de destino

        # Matrizes 1-based: [0] é espaço não utilizado
        self.capacity = [[0] * (self.n + 1) for _ in range(self.n + 1)]  # ū(i, j)
        self.lower = [[0] * (self.n + 1) for _ in range(self.n + 1)]     # u(i, j)
        self.cost = [[0] * (self.n + 1) for _ in range(self.n + 1)]      # custo(i, j)
        self.flow = [[0] * (self.n + 1) for _ in range(self.n + 1)]      # f(i, j)

    def add_edge(self, u, v, cap, cost=0, lower=0):
        self.graph.add_edge(u, v, cost)
        self.capacity[u][v] = cap
        self.lower[u][v] = lower
        self.cost[u][v] = cost

    def imprimir_fluxo_atual(self):
        """
        Imprime o fluxo atual nas arestas do grafo.
        """
        print("\nArestas da Rede de Fluxo:")

        print("\n🔍 Arestas da Rede de Fluxo (S = origem, T = destino):\n")
        for u in range(1, self.n + 1):
            for v in range(1, self.n + 1):
                cap = self.capacity[u][v]
                cost = self.cost[u][v]
                lower = self.lower[u][v]
                if cap > 0 or lower > 0 or cost != 0:
                    rotulo_u = "S" if u == self.source else ("T" if u == self.sink else str(u))
                    rotulo_v = "S" if v == self.source else ("T" if v == self.sink else str(v))
                    print(f"De {rotulo_u} para {rotulo_v}: capacidade = {cap}, custo = {cost}, limite inferior = {lower}")
        
