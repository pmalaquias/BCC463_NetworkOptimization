# Grafo estruturado como lista de adjacências

class Graph:
    """Classe que representa um grafo"""
    #n = número de vértices
    #directed = grafo direcionado ou não
    #adj = lista de adjacências
    #capacity = capacidade das arestas
    #explored_edges = arestas exploradas

    def __init__(self, n, directed):
        self.n = n # número de vértices
        self.directed = directed # grafo direcionado ou não
        self.adj = [[] for _ in range(n + 1)] # lista de adjacências
        self.capacity = {} # capacidade das arestas
        self.explored_edges = set() #
        
    def add_edge(self, u, v, w):
        """Adiciona uma aresta de u para v com peso w"""
        self.adj[u].append(v)
        self.adj[v].append(u) #Adiciona uma aresta reverso para o grafo residual
        self.capacity[(u, v)] = w
        if not self.directed: # se o grafo não é direcionado
            self.adj[v].append(u)
            self.capacity[(v, u)] = w

    def show_graph(self):
        for u in range(self.n):
            print(u, end=' -> ')
            for v in self.adj[u]:
                print(v, end=' ')
            print()
        