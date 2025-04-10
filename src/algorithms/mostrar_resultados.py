from algorithms.reconstruir_caminho import BuildPath


def MostrarResultado(dt, rot, origem):
    """
    Exibe os resultados dos caminhos mais curtos de um nó de origem para todos os outros nós.

    Args:
        dt (dict): Um dicionário onde as chaves são nós de destino e os valores são as menores distâncias a partir do nó de origem.
        rot (dict): Um dicionário onde as chaves são nós de destino e os valores são o nó precedente no caminho mais curto.
        origem (any): O nó de origem a partir do qual os caminhos mais curtos são calculados.

    Comportamento:
        - Itera por todos os nós de destino em ordem crescente.
        - Ignora o nó de origem e nós com distância infinita.
        - Constrói o caminho para cada destino usando a função `BuildPath`.
        - Imprime o nó de destino, sua menor distância e o caminho como uma string formatada.
    """
    for destino in sorted(dt.keys()):
        if destino != origem and dt[destino] != float('inf'):
            caminho = BuildPath(rot, destino)
            print(f"{destino} ({dt[destino]}) : {' '.join(map(str, caminho))}")