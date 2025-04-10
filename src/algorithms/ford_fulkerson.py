from collections import deque


def FordFulkerson(flow, s, t):
    n = flow.n
    f = [[0] * (n + 1) for _ in range(n + 1)]
    max_flow = 0
    caminhos = []  # Aqui armazenamos os caminhos

    while True:
        label = [None] * (n + 1)
        label[s] = (-1, '+', float('inf'))

        q = deque()
        q.append(s)

        while q and label[t] is None:
            u = q.popleft()
            for v in flow.graph.adj[u]:
                # Direto
                if label[v] is None and flow.capacity[u][v] - f[u][v] > 0:
                    xi = min(label[u][2], flow.capacity[u][v] - f[u][v])
                    label[v] = (u, '+', xi)
                    q.append(v)
                # Reverso
                elif label[v] is None and f[v][u] > flow.lower[v][u]:
                    xi = min(label[u][2], f[v][u] - flow.lower[v][u])
                    label[v] = (u, '-', xi)
                    q.append(v)

        if label[t] is None:
            break

        # Aumenta fluxo e registra caminho
        caminho = []
        direcoes = []
        xi_t = label[t][2]
        v = t

        while v != s:
            u, tipo, _ = label[v]
            if tipo == '+':
                f[u][v] += xi_t
            else:
                f[v][u] -= xi_t
            caminho.append(v)
            direcoes.append(tipo)
            v = u
        caminho.append(s)
        caminho.reverse()
        direcoes.reverse()

        caminhos.append((caminho, direcoes, xi_t))
        max_flow += xi_t

    return max_flow, f, caminhos