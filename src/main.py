
import os

from algorithms.BellmanFord import BellmanFord
from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.Dijkstra import Dijkstra
from algorithms.graph import Graph
from algorithms.Johnson import johnson
from algorithms.mostrar_resultados import mostrar_resultado
from utils.load_graph import load_graph
from utils.menu import menu
from utils.readFile import read_file


def main():

    menu()
    menu_option = int(input("Digite sua opção: "))

    while menu_option != 0:

        if menu_option < 0 or menu_option > 6:
            print("Opção inválida!")
            menu()
            menu_option = int(input("Digite sua opção: "))
            continue

        # Carregar o grafo com base na opção do menu
        g, i = load_graph(menu_option, read_file, Graph)


        match menu_option:
            case 1:
                print('Grafo:')
                g.show_graph()
            case 2:
                print("DFS:")
                visited = [False] * (g.n + 1)
                result = []
                DFS(g, i, visited, result)
                print(" ".join(map(str, result)))
            case 3:
                print("BFS:")
                BFS(g, i)
            case 4:
                print("Dijkstra:")
                dt, rot = Dijkstra(g, i)
                mostrar_resultado(dt, rot, i)
            case 5:
                print("Bellman-Ford:")
                dt, rot, has_negative_cycle = BellmanFord(g, i)
                if not has_negative_cycle:
                    mostrar_resultado(dt, rot, i)
            case 6:
                print("Johnson:")
                matriz = johnson(g)
                if matriz:
                    for linha in matriz:
                        print(' '.join(str(int(x)) if x != float('inf') else 'INF' for x in linha))

        print("\n")
        menu()
        menu_option = int(input("Digite sua opção: "))
       

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    #print('This is the main module')
    main() 