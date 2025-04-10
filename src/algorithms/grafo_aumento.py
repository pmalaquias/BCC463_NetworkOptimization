from algorithms.flow import Flow


def AugmentingGraph(flow: Flow):
    G = []

    for u in range(1, flow.n + 1):
        for v in flow.graph.adj[u]:
            f = flow.flow[u][v]
            c = flow.capacity[u][v]
            l = flow.lower[u][v]

            if f < c:  # Arco direto
                G.append((u, v, 'direto', c - f))
            if f > l:  # Arco reverso
                G.append((v, u, 'reverso', f - l))

    return G