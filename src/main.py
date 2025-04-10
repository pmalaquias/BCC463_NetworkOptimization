
import os

from algorithms.bellman_ford import BellmanFord
from algorithms.BFS import BFS
from algorithms.circulacao_viavel import (ValidateCirculationFlow,
                                          corte_minimo, grafo_de_aumento)
from algorithms.DFS import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.dinitz import Dinitz
from algorithms.ford_fulkerson import FordFulkerson
from algorithms.graph import Graph
from algorithms.johnson import Johnson
from algorithms.mostrar_resultados import MostrarResultado
from algorithms.reconstruir_caminho import BuildPath
from utils.exibir_graficamente import (destacar_caminho_mais_curto,
                                       exibir_grafo_de_aumento,
                                       exibir_grafo_graficamente)
from utils.load_graph import load_graph
from utils.menu import menu
from utils.readFile import read_file


def main():

    menu()
    menu_option = int(input("Digite sua opção: "))

    while menu_option != 0:

        if menu_option < 0 or menu_option > 13:
            print("Opção inválida!")
            menu()
            menu_option = int(input("Digite sua opção: "))
            continue

        if menu_option <= 6:
            # Carregar o grafo com base na opção do menu
            g, i = load_graph(menu_option, read_file, Graph)
        else:
            # Carregar o grafo para fluxo
            f = load_graph(menu_option, read_file, Graph)


        match menu_option:
            case 1:
                print('Grafo:')
                g.show_graph()
                exibir_grafo_graficamente(g)
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
                # Supondo que 'grafo' foi carregado com load_graph e é do tipo Graph
                dt, rot = Dijkstra(g, i)

                destino = int(input("Digite o vértice de destino: "))
                caminho = BuildPath(rot, destino)

                print(f"\n Caminho mais curto até {destino}: {' → '.join(map(str, caminho))}")
                print(f" Distância total: {dt[destino]}")

                # Destaca o caminho mais curto no grafo
                destacar_caminho_mais_curto(g, caminho)

                # Exibe graficamente
                exibir_grafo_graficamente(g)

            case 5:
                print("Bellman-Ford:")
                dt, rot, has_negative_cycle = BellmanFord(g, i)
                if not has_negative_cycle:
                    destino = int(input("Digite o vértice de destino: "))
                    caminho = BuildPath(rot, destino)
                    print(f"\n Caminho mais curto até {destino}: {' → '.join(map(str, caminho))}")
                    print(f" Distância total: {dt[destino]}")
                    # Destaca o caminho mais curto no grafo
                    destacar_caminho_mais_curto(g, caminho)
                    # Exibe graficamente
                    exibir_grafo_graficamente(g)
                    MostrarResultado(dt, rot, i)
            case 6:
                print("Johnson:")
                matriz = Johnson(g)
                if matriz:
                    for linha in matriz:
                        print(' '.join(str(int(x)) if x != float('inf') else 'INF' for x in linha))
            case 7:
                print("Fluxo:")
                f.imprimir_fluxo_atual()
                exibir_grafo_graficamente(f)
            case 8:
                print("Verificando fluxo viável:")
                f.verificar_fluxo_viavel()
                f.imprimir_fluxo_atual()
                ok = ValidateCirculationFlow(f)
                if ok:
                    print("Fluxo viável encontrado.")
                    exibir_grafo_graficamente(f)
                else:
                    print("Fluxo inviável.")
            case 9:
                print("Fluxo Máximo:")
                valor, f_result, _ = FordFulkerson(f, f.source, f.terminal)
                f.flow = f_result
                print(f"Fluxo máximo entre {f.source} e {f.terminal}: {valor}")
                exibir_grafo_graficamente(f)

            case 10:
                print("Corte Mínimo:")
                valor, f_result, _ = FordFulkerson(f, f.source, f.terminal)
                corte = corte_minimo(f, f.source, f_result)
                print("Corte mínimo (arestas):")
                for u, v in corte:
                    print(f"{u} -> {v} (capacidade = {f.capacity[u][v]})")

            case 11:
                print("Grafo de Aumento de Fluxo:")
                # Executa fluxo máximo para gerar fluxo válido
                valor, f_result, caminhos = FordFulkerson(f, f.source, f.terminal)
                f.flow = f_result

                aumento = grafo_de_aumento(f)

                print("Grafo de Aumento de Fluxo:")
                for u, v, tipo, folga in aumento:
                    print(f"{u} -> {v} ({tipo}) - folga: {folga}")

                # Exibe o grafo original com fluxo
                exibir_grafo_graficamente(f)

                # Exibe graficamente o grafo de aumento
                exibir_grafo_de_aumento(f, aumento)
            case 12:
                print("Ford-Fulkerson:")
                valor, f_result, caminhos = FordFulkerson(f, f.source, f.terminal)
                f.flow = f_result
                print(f"Fluxo máximo entre {f.source} e {f.terminal}: {valor}")
                print("Caminhos de aumento utilizados:\n")
                for caminho, tipos, fluxo in caminhos:
                    rotas = []
                    for i in range(len(caminho) - 1):
                        u, v = caminho[i], caminho[i + 1]
                        seta = '→' if tipos[i] == '+' else '←'
                        rotas.append(f"{u} {seta} {v}")
                    print("   " + "  ".join(rotas) + f"   (fluxo aumentado: {fluxo})")
                exibir_grafo_graficamente(f)

            case 13:
                print("Dinitz:")
                maxflow = Dinitz(f)
                print(f"Fluxo máximo com Dinitz: {maxflow}")
                exibir_grafo_graficamente(f)
       

        print("\n")
        menu()
        menu_option = int(input("Digite sua opção: ")) or 0
       

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    #print('This is the main module')
    main() 