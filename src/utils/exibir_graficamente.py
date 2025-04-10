import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout  # usa pygraphviz


def destacar_caminho_mais_curto(grafo, caminho):
    """
    Marca as arestas do caminho mais curto com atributo 'color' para serem desenhadas em vermelho.
    """
    grafo.caminho_destacado = set()
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        grafo.caminho_destacado.add((u, v))



def exibir_grafo_graficamente(grafo, fluxo_maximo=None, caminho_mais_curto=None):
    """
    Exibe graficamente grafos simples ou redes de fluxo.
    - Suporta Flow ou Graph
    - Exibe fluxo/capacidade, custo e limite inferior
    - Destaca vértices source (S) e sink (T)
    """

    is_flow = hasattr(grafo, 'flow') and hasattr(grafo, 'capacity')
    is_directed = grafo.directed if hasattr(grafo, 'directed') else grafo.graph.directed
    base = grafo if hasattr(grafo, 'adj') else grafo.graph  # para acessar .adj e .n

    G = nx.DiGraph() if is_directed else nx.Graph()
    n = base.n

    # Garante que todos os nós sejam adicionados, mesmo os isolados
    for node in range(1, n + 1):
        G.add_node(node)

    edge_labels = {}

    for u in range(1, n + 1):
        for v in base.adj[u]:
            if is_directed or u < v:
                G.add_edge(u, v)

                # Verifica se a aresta faz parte do caminho mais curto
                if hasattr(grafo, "caminho_destacado") and (u, v) in grafo.caminho_destacado:
                    G[u][v]["color"] = "red"
                else:
                    G[u][v]["color"] = "black"

                if is_flow:
                    f = grafo.flow[u][v]
                    c = grafo.capacity[u][v]
                    cost = grafo.cost[u][v]
                    lower = grafo.lower[u][v]
                    #edge_labels[(u, v)] = f"f/c: {f}/{c}\nc: {cost} li: {lower}"
                    if c > 0 or f > 0:  # mostra arestas com capacidade ou fluxo
                        G.add_edge(u, v)
                        edge_labels[(u, v)] = f"[{f}, {c}]"
                else:
                    weight = base.capacity.get((u, v), "") if hasattr(base, 'capacity') else ""
                    edge_labels[(u, v)] = f"{weight}" if weight != "" else ""

    try:
        pos =graphviz_layout(G, prog='neato')  # usa layout hierárquico (top-down)
        #print("Usando layout do Graphviz")
    except:
        pos = nx.spring_layout(G, seed=42)  # fallback se não tiver pygraphviz

    #  Cores e labels dos nós
    node_colors = []
    node_labels = {}

    for node in G.nodes:
        if is_flow and node == grafo.source:
            node_colors.append("green")
            node_labels[node] = "S"
        elif is_flow and node == grafo.sink:
            node_colors.append("red")
            node_labels[node] = "T"
        else:
            node_colors.append("lightblue")
            node_labels[node] = str(node)

    # Define cor de cada aresta (vermelho para caminho mais curto, preto padrão)
    edge_colors = []
    for u, v in G.edges:
        color = G[u][v].get("color", "black")
        edge_colors.append(color)

    nx.draw(G, pos,
            labels=node_labels,
            with_labels=True,
            node_color=node_colors,
            node_size=800,
            arrows=bool(is_directed),
            edge_color=edge_colors,
            width=2)
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black", font_size=8)

    # Título
    if is_flow:
        plt.title("Rede de Fluxo (f/c, custo, li)")
    elif is_directed:
        plt.title("Grafo Direcionado")
    else:
        plt.title("Grafo Não Direcionado")

    plt.axis("off")
    plt.show(block = False) # Não bloqueia o loop do programa
    plt.pause(3)  # Pausa para garantir que a janela seja exibida
    plt.close()  # Fecha a janela após exibir o grafo

def exibir_grafo_de_aumento(grafo, aumento):
    """
    Exibe o grafo de aumento com:
    -  Arcos diretos
    -  Arcos reversos
    - Setas visíveis
    """
    G = nx.DiGraph()
    n = grafo.n

    for node in range(1, n + 1):
        G.add_node(node)

    edge_labels = {}
    edge_colors = []

    for u, v, tipo, folga in aumento:
        G.add_edge(u, v)
        edge_labels[(u, v)] = f"[{tipo[0].upper()}] {folga}"
        edge_colors.append("blue" if tipo == "direto" else "red")

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=800)
    nx.draw_networkx_labels(G, pos, font_weight='bold')

    # Desenha as arestas com setas visíveis
    for (u, v), color in zip(G.edges(), edge_colors):
        nx.draw_networkx_edges(
            G, pos,
            edgelist=[(u, v)],
            edge_color=color,
            arrowstyle='-|>',
            arrowsize=25,
            connectionstyle='arc3,rad=0.1',
            width=2
        )

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    plt.title("Grafo de Aumento de Fluxo ( direto /  reverso)")
    plt.axis("off")
    plt.tight_layout()
    plt.show()