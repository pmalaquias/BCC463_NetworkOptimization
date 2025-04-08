import os


def load_graph(menu_option: int, read_file, Graph):
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    subpath = "../../input/"
    # Caminho do arquivo no diretório ../../input/
    # Exemplo: ../../input/input1.txt


    if menu_option != 6:
        # Algoritmos de 1 a 5 → input1.txt até input4.txt
        file_name = input("Digite o nome do arquivo de entrada (ex: input2.txt): ") or "input1.txt"
        caminho_arquivo = os.path.join(diretorio_base, "../../input/", file_name)

        entrada = read_file(caminho_arquivo)
        n, m, b, i = map(int, entrada[0].split())
        g = Graph(n, directed=b)

    else:
        # Algoritmo de Johnson → input5.txt até input11.txt
        file_name = input("Digite o nome do arquivo de entrada (ex: input5.txt): ") or "input5.txt"
        caminho_arquivo = os.path.join(diretorio_base, "../../input/", file_name)

        entrada = read_file(caminho_arquivo)
        n, m = map(int, entrada[0].split())
        g = Graph(n, directed=True)

    # Adiciona as arestas
    for row in entrada[1:]:
        u, v, w = map(int, row.split())
        g.add_edge(u, v, w)

    return g, i # retorna o grafo carregado e o vértice inicial