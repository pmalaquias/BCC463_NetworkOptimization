
from algorithms.graph import Graph


class Flow:
    """
    Class Flow
    Esta classe representa uma rede de fluxo e fornece métodos para gerenciar e verificar fluxos
    em um grafo direcionado com capacidades, custos e limites inferiores.

    Atributos:
        graph (Graph): O objeto grafo que representa a rede.
        n (int): O número de vértices no grafo.
        source (int): O vértice de origem na rede de fluxo.
        terminal (int): O vértice terminal (destino) na rede de fluxo.
        capacity (list[list[int]]): Uma matriz 2D representando os limites superiores de capacidade das arestas.
        lower (list[list[int]]): Uma matriz 2D representando os limites inferiores de capacidade das arestas.
        cost (list[list[int]]): Uma matriz 2D representando o custo associado às arestas.
        flow (list[list[int]]): Uma matriz 2D representando o fluxo atual nas arestas.

    Métodos:
        __init__(graph: Graph, source: int, terminal: int):
            Inicializa o objeto Flow com um grafo, vértice de origem e vértice terminal.
        add_edge(u: int, v: int, cap: int, cost: int = 0, lower: int = 0):
            Adiciona uma aresta à rede de fluxo com capacidade, custo e limite inferior especificados.
        verificar_fluxo_viavel() -> bool:
            Verifica se o fluxo atual é viável, verificando:
            1. Se o fluxo respeita os limites inferior e superior.
            2. Se o fluxo é conservativo para todos os vértices, exceto origem e terminal.
        imprimir_fluxo_atual():
            Imprime o fluxo atual nas arestas da rede de fluxo, incluindo capacidades,
            custos e limites inferiores.
    """
    def __init__(self, graph: Graph, source: int, terminal: int):
        self.graph = graph
        self.n = graph.n

        self.source = source  # vértice de origem
        self.terminal = terminal      # vértice de destino

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

    def verificar_fluxo_viavel(self):
        """
        Verifica se o fluxo atual é viável:
        1. Respeita os limites inferior e superior
        2. É conservativo para todos os vértices (exceto s e t)
        """
        print("\nVerificando fluxo viável:")

        # 1. Verificar se o fluxo está entre os limites
        for u in range(1, self.n + 1):
            for v in range(1, self.n + 1):
                f = self.flow[u][v]
                lower = self.lower[u][v]
                upper = self.capacity[u][v]
                if f < lower or f > upper:
                    print(f"Fluxo de {u} para {v} = {f} está fora dos limites [{lower}, {upper}]")
                    return False

        # 2. Verificar conservação do fluxo (exceto source e sink)
        for v in range(1, self.n + 1):
            if v == self.source or v == self.terminal:
                continue

            entrada = sum(self.flow[u][v] for u in range(1, self.n + 1))
            saida = sum(self.flow[v][w] for w in range(1, self.n + 1))

            if entrada != saida:
                print(f" Violação da conservação no vértice {v}: entrada = {entrada}, saída = {saida}")
                return False

        print(" O fluxo atual é viável (respeita os limites e é conservativo).")
        return True


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
                    rotulo_u = "S" if u == self.source else ("T" if u == self.terminal else str(u))
                    rotulo_v = "S" if v == self.source else ("T" if v == self.terminal else str(v))
                    print(f"De {rotulo_u} para {rotulo_v}: capacidade = {cap}, custo = {cost}, limite inferior = {lower}")
        
