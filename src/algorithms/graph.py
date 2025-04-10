# Grafo estruturado como lista de adjacências

class Graph:
    """""
    Graph class represents a graph data structure with support for directed and undirected graphs.
    Attributes:
        n (int): Number of vertices in the graph.
        directed (bool): Indicates whether the graph is directed or not.
        adj (list of list): Adjacency list representation of the graph.
        capacity (dict): Dictionary storing the capacity (weight) of edges as key-value pairs.
        explored_edges (set): Set to keep track of explored edges.
    Methods:
        __init__(n, directed):
            Initializes the graph with the given number of vertices and directionality.
        add_edge(u, v, w):
            Adds an edge from vertex u to vertex v with weight w. If the graph is undirected,
            it also adds the reverse edge.
        show_graph():
    """""

    def __init__(self, n: int, directed = False):
        self.n = n # número de vértices
        self.directed = directed # grafo direcionado ou não
        self.adj = [[] for _ in range(n + 1)] # lista de adjacências
        self.capacity = {} # capacidade das arestas
        self.explored_edges = set() #
        
    def add_edge(self, u, v, w):
        """Adiciona uma aresta de u para v com peso w"""
        self.adj[u].append(v)
        #self.adj[v].append(u) #Adiciona uma aresta reverso para o grafo residual
        self.capacity[(u, v)] = w
        if not self.directed: # se o grafo não é direcionado
            self.adj[v].append(u)
            self.capacity[(v, u)] = w

    def show_graph(self):
        """
        Displays the adjacency list representation of the graph.

        For each vertex in the graph, this method prints the vertex followed by
        the list of its adjacent vertices.

        Example output for a graph with 3 vertices and edges (0 -> 1, 0 -> 2, 1 -> 2):
            0 -> 1 2
            1 -> 2
            2 ->

        """

        if(self.directed):
            print('Grafo direcionado:')
            for u in range(self.n):
                print(u+1, end=' -> ') #imprime o vértice 
                for v in self.adj[u+1]:
                    print(v, end=' ') #imprime os vértices adjacentes
                print()
        else:
            print('Grafo não direcionado:')
            for u in range(self.n):
                print(u+1, end=' -> ')
                for v in self.adj[u+1]:
                    print(v, end=' ')
                print()