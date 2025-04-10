import os

from algorithms.flow import Flow


def load_graph(menu_option: int, read_file, Graph):
    """
    Carrega um grafo ou uma rede de fluxo com base na opção de menu selecionada e no arquivo de entrada.
    Parâmetros:
        menu_option (int): A opção de menu selecionada pelo usuário, que determina o tipo de grafo ou rede de fluxo a ser carregado.
        read_file (callable): Uma função para ler o arquivo de entrada e retornar seu conteúdo como uma lista de strings.
        Graph (class): Uma classe que representa a estrutura de um grafo, usada para criar instâncias de grafos.
    Retorna:
        tuple ou objeto:
            - Para menu_option 1, 2-5 ou outros casos: Retorna uma tupla (g, i), onde:
                - g: Uma instância da classe Graph representando o grafo carregado.
                - i: Um inteiro representando o vértice inicial ou None, se não aplicável.
            - Para menu_option >= 7: Retorna uma instância da classe Flow representando a rede de fluxo carregada.
    Lança:
        ValueError: Se o formato do arquivo de entrada for inválido ou não corresponder à estrutura esperada.
    Notas:
        - A função suporta diferentes tipos de grafos com base na opção de menu:
            - menu_option 1: Carrega um grafo com arestas opcionais direcionadas e um vértice inicial.
            - menu_option 2-5: Carrega um grafo direcionado com pesos.
            - menu_option >= 7: Carrega uma rede de fluxo com capacidades, custos e fluxos iniciais opcionais.
            - Outros casos: Carrega um grafo direcionado para algoritmos como o algoritmo de Johnson.
        - Os arquivos de entrada devem estar localizados no diretório "../../input/" relativo à localização do script.
        - O usuário é solicitado a inserir o nome do arquivo, com um valor padrão fornecido caso nenhuma entrada seja dada.
    """
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    subpath = "../../input/"


    if menu_option == 1:
        # Algoritmo de Exibir Grafo → input1.txt até input4.txt
        list_available_files(menu_option)

        file_name = input("Digite o nome do arquivo de entrada (ex: input1.txt): ") or "input1.txt"
        caminho_arquivo = os.path.join(current_file_directory, subpath, file_name)

        entrada = read_file(caminho_arquivo)

        dados = len(list(entrada[0].split()))

        if dados == 4:
            n, m, b, i = map(int, entrada[0].split())
            g = Graph(n, directed=b)
        elif dados == 2:
            n, m = map(int, entrada[0].split())
            i = None
            g = Graph(n, directed=True)
        else:
            n, m, s, t = map(int, entrada[0].split())
            i = None
            g = Graph(n, directed=True)

        for row in entrada[1:]:
            u, v, w = map(int, row.split())
            g.add_edge(u, v, w)

        print(f"Abrindo o arquivo: {file_name}")
        return g, i
    
    elif menu_option >= 7:
        # Algoritmos de 7 a 9 → input1.txt até input4.txt
        list_available_files(menu_option)

        file_name = input("Digite o nome do arquivo de entrada (ex: input12.txt): ") or "input12.txt"
        caminho_arquivo = os.path.join(current_file_directory, "../../input/", file_name)

        entrada = read_file(caminho_arquivo)
        n, m, s, t = map(int, entrada[0].split())
        g = Graph(n, directed=True)
        f = Flow(g, s, t)
        for row in entrada[1:]:
            dados = list(map(int, row.split()))

            if len(dados) == 6:
                # Caso tenha limite inferior
                u, v, cap, cost, lower, flow_val = dados
            else:
                u, v, cap, cost, lower = dados
                flow_val = 0  # Valor de fluxo padrão se não for fornecido

            f.add_edge(u  , v , cap, cost, lower)
            f.flow[u][v] = flow_val  # Adiciona o fluxo inicial (se fornecido)

        print(f"Abrindo o arquivo: {file_name}")

        return f  # Retorna a instância de Flow


    elif menu_option in range(2, 6):
        # Algoritmos de 1 a 5 → input1.txt até input4.txt
        list_available_files(menu_option)

        file_name = input("Digite o nome do arquivo de entrada (ex: input2.txt): ") or "input1.txt"
        caminho_arquivo = os.path.join(current_file_directory, "../../input/", file_name)

        entrada = read_file(caminho_arquivo)
        n, m, b, i = map(int, entrada[0].split())
        g = Graph(n, directed=b)

        for row in entrada[1:]:
            u, v, w = map(int, row.split())
            g.add_edge(u, v, w)

        print(f"Abrindo o arquivo: {file_name}")
        return g, i

    else:
        # Algoritmo de Johnson → input5.txt até input11.txt
        list_available_files(menu_option)

        file_name = input("Digite o nome do arquivo de entrada (ex: input5.txt): ") or "input5.txt"
        caminho_arquivo = os.path.join(current_file_directory, "../../input/", file_name)

        entrada = read_file(caminho_arquivo)
        n, m = map(int, entrada[0].split())
        i = None
        g = Graph(n, directed=True)

        # Adiciona as arestas
        for row in entrada[1:]:
            u, v, w = map(int, row.split())
            g.add_edge(u, v, w)

        print(f"Abrindo o arquivo: {file_name}")
        return g, i # retorna o grafo carregado e o vértice inicial
    


def list_available_files(menu_option: int):
    base_directory = os.path.dirname(os.path.abspath(__file__))
    caminho_input = os.path.join(base_directory, "../../input")

    # Define os intervalos válidos conforme a opção
    if menu_option == 1:
        faixa_valida = range(1, 100)     # input1 a input4
    elif menu_option >= 7:
        faixa_valida = range(12, 100)  # input12 em diante
    elif menu_option == 6:
        faixa_valida = range(5, 12)    # input5 a input11
    else:
        faixa_valida = range(1, 5)     # input1 a input4

    available_files = []

    for arquivo in os.listdir(caminho_input):
        if arquivo.startswith("input") and arquivo.endswith(".txt"):
            try:
                numero = int(arquivo.replace("input", "").replace(".txt", ""))
                if numero in faixa_valida:
                    available_files.append(arquivo)
            except ValueError:
                continue

    if available_files:
        print("\n📄 Arquivos disponíveis para essa opção:")
        for arq in sorted(available_files):
            print(f"  - {arq}")
    else:
        print("\n⚠️ Nenhum arquivo disponível para essa opção.")

    return available_files