from algorithms.reconstruir_caminho import reconstruir_caminho


def mostrar_resultado(dt, rot, origem):
    """Exibe os resultados no formato desejado."""
    for destino in sorted(dt.keys()):
        if destino != origem and dt[destino] != float('inf'):
            caminho = reconstruir_caminho(rot, destino)
            print(f"{destino} ({dt[destino]}) : {' '.join(map(str, caminho))}")