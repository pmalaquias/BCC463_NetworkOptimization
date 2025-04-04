def reconstruir_caminho( rot, destino):
    caminho =[]
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = rot[atual]
    return caminho[::-1]