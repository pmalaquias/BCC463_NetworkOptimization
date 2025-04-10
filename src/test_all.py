from algorithms.bellman_ford import BellmanFord
from algorithms.BFS import BFS
from algorithms.circulacao_viavel import (ValidateCirculationFlow,
                                          corte_minimo, grafo_de_aumento)
from algorithms.DFS import DFS
from algorithms.Dijkstra import Dijkstra
from algorithms.Dinitz import dinitz
from algorithms.ford_fulkerson import FordFulkerson
from algorithms.Johnson import johnson
from utils.load_graph import load_graph
from utils.readFile import read_file


def listar_arquivos_validos(menu_option):
    if 1 <= menu_option <= 5:
        return [f"input{i}.txt" for i in range(1, 5)]
    elif menu_option == 6:
        return [f"input{i}.txt" for i in range(5, 12)]
    elif menu_option >= 7:
        return [f"input{i}.txt" for i in range(12, 30)]
    return []

def testar_algoritmo(menu_option, file_name):
    print(f"\n🔍 Testando algoritmo {menu_option} com {file_name}")
    try:
        entrada, valor_inicial = load_graph(menu_option, read_file, None, override_filename=file_name)

        match menu_option:
            case 1:
                print('Grafo:')
                entrada.show_graph()
                entrada.exibir_grafo_graficamente()
            case 2:
                visited = [False] * (entrada.n + 1)
                result = []
                DFS(entrada, valor_inicial, visited, result)
                print("DFS:", result)
            case 3:
                print("BFS:")
                BFS(entrada, valor_inicial)
            case 4:
                print("Dijkstra:")
                dt, rot = Dijkstra(entrada, valor_inicial)
                print(dt)
            case 5:
                print("Bellman-Ford:")
                dt, rot, neg = BellmanFord(entrada, valor_inicial)
                print(dt)
            case 6:
                print("Johnson:")
                matriz = johnson(entrada)
                print(matriz)
            case 7:
                print("Fluxo Viável:")
                entrada.verificar_fluxo_viavel()
            case 8:
                print("Circulação:")
                ValidateCirculationFlow(entrada)
            case 9:
                print("Ford-Fulkerson:")
                valor, f_result, _ = FordFulkerson(entrada, entrada.source, entrada.sink)
                print("Fluxo máximo:", valor)
            case 10:
                print("Corte Mínimo:")
                valor, f_result, _ = FordFulkerson(entrada, entrada.source, entrada.sink)
                corte = corte_minimo(entrada, entrada.source, f_result)
                print("Corte mínimo:", corte)
            case 11:
                print("Grafo de Aumento:")
                _, f_result, _ = FordFulkerson(entrada, entrada.source, entrada.sink)
                entrada.flow = f_result
                aumento = grafo_de_aumento(entrada)
                print("Aumento:", aumento)
            case 12:
                print("Ford-Fulkerson:")
                valor, f_result, caminhos = FordFulkerson(entrada, entrada.source, entrada.sink)
                print("Fluxo máximo:", valor)
            case 13:
                print("Dinitz:")
                maxflow = dinitz(entrada)
                print("Fluxo máximo com Dinitz:", maxflow)

    except Exception as e:
        print(f"❌ Erro: {e}")

def main():
    for menu_option in range(2, 14):
        arquivos = listar_arquivos_validos(menu_option)
        for file_name in arquivos:
            testar_algoritmo(menu_option, file_name)

if __name__ == "__main__":
    main()