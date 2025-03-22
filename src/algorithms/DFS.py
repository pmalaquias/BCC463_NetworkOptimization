
from algorithms.graph import Graph


def DFS(graph: Graph, v: int, visited, result):
    """
    Performs a Depth-First Search (DFS) on a graph starting from a given vertex.
    Args:
        graph (Graph): The graph object containing adjacency list and explored edges.
        v (int): The current vertex being visited.
        visited (list[bool]): A list indicating whether each vertex has been visited.
        result (list[int]): A list to store the order of visited vertices.
    Side Effects:
        - Marks the current vertex as visited.
        - Appends the current vertex to the result list.
        - Explores edges and adds them to the set of explored edges in the graph.
    Notes:
        - If an edge is already in the set of explored edges, it will not be added again.
        - The function is recursive and will continue exploring unvisited adjacent vertices.
    """
    """Realiza a busca em profundidade (DFS)"""
    visited[v] = True
    result.append(v)
    
    for w in graph.adj[v]:
        if not visited[w]:
            graph.explored_edges.add((v, w))  # Explorar aresta
            DFS(graph, w, visited, result)
        elif (v, w) not in graph.explored_edges:
            graph.explored_edges.add((v, w))  # Explorar aresta
