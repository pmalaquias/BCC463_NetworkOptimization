from collections import deque

from algorithms.flow import Flow
from algorithms.ford_fulkerson import FordFulkerson
from algorithms.graph import Graph


def ValidateCirculationFlow(flow: Flow) -> bool:

    n = flow.n
    g_original = flow.graph
    V = list(range(1, n + 1))

    # Define índices para s' e t'
    s_ = n + 1
    t_ = n + 2
    H = Graph(n + 2, directed=True)
    f_H = Flow(H, s_, t_)

    # Copia a estrutura base
    f_H.source = s_
    f_H.terminal = t_

    # Adiciona arcos (i, j) com capacidade ū(i,j) - u(i,j)
    for i in V:
        for j in V:
            cap_ij = flow.capacity[i][j] - flow.lower[i][j]
            if cap_ij > 0:
                f_H.add_edge(i, j, cap_ij)

    # Arcos (s', i) com capacidade = soma dos limites inferiores que entram em i
    for i in V:
        entrada = sum(flow.lower[j][i] for j in V)
        if entrada > 0:
            f_H.add_edge(s_, i, entrada)

    # Arcos (i, t') com capacidade = soma dos limites inferiores que saem de i
    for i in V:
        saida = sum(flow.lower[i][j] for j in V)
        if saida > 0:
            f_H.add_edge(i, t_, saida)

    # Arco (t, s) com capacidade ∞
    f_H.add_edge(flow.terminal, flow.source, float('inf'))

    # Aplica fluxo máximo em H (usando Edmonds-Karp, Ford-Fulkerson, etc)
    max_flow, f_result, _ = FordFulkerson(f_H, s_, t_)  # ← você pode trocar pelo seu algoritmo

    # Verifica se todos os arcos (s', i) estão saturados
    demanda_total = sum(
        f_H.capacity[s_][i] for i in V if f_H.capacity[s_][i] > 0
    )

    if max_flow < demanda_total:
        print("Circulação inviável: não foi possível saturar todos os arcos de s'.")
        return False

    # Atualiza os fluxos originais
    for i in V:
        for j in V:
            flow.flow[i][j] = f_result[i][j] + flow.lower[i][j]

    print("Circulação viável encontrada e fluxo atualizado com sucesso.")
    return True



