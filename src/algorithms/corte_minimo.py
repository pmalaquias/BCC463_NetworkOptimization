from collections import deque


def get_min_cut_edges(flow, source, f_result):

    n = flow.n
    visited = [False] * (n + 1)
    q = deque()
    q.append(source)
    visited[source] = True

    while q:
        u = q.popleft()
        for v in flow.graph.adj[u]:
            if not visited[v] and flow.capacity[u][v] - f_result[u][v] > 0:
                visited[v] = True
                q.append(v)

    # X são os visitados, X̄ os não visitados
    corte = []
    for u in range(1, n + 1):
        if visited[u]:
            for v in flow.graph.adj[u]:
                if not visited[v] and flow.capacity[u][v] > 0:
                    corte.append((u, v))

    return corte