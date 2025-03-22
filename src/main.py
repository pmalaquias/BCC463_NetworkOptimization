
import os

from algorithms.DFS import DFS
from algorithms.graph import Graph
from algorithms.readFile import read_file


def main():
    # Caminho do arquivo no diretório ../input/
    diretorio_base = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
    caminho_arquivo = os.path.join(diretorio_base, "../input/input2.txt")



    entrada = read_file(caminho_arquivo)

    # Processamento dos dados de entrada
    n, m, b, i = map(int, entrada[0].split()) #lendo os valores de n, m, b e i
    g = Graph(n, directed=bool(b)) #criando o grafo

    for row in entrada[1:]:
        u, v, w = map(int, row.split())
        g.add_edge(u, v, w)

    #mostrando o grafo
    print('Grafo:')
    g.show_graph()

    #realizando a busca em profundidade
    print("DFS:")
    visited = [False] * (g.n + 1)
    result = []
    DFS(g, i, visited, result)
    print(" ".join(map(str, result)))




if __name__ == '__main__':
    print('This is the main module')
    main() 