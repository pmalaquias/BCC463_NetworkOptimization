def BuildPath( rot, destino):
    """
        Reconstrói o caminho de um nó de origem até um nó de destino usando um dicionário de roteamento.

        Argumentos:
            rot (dict): Um dicionário onde as chaves são nós e os valores são o nó precedente 
                        no caminho até a origem. O valor para o nó de origem deve ser None.
            destino: O nó de destino para o qual o caminho será reconstruído.

        Retorna:
            list: Uma lista de nós representando o caminho da origem até o destino, 
                  em ordem da origem para o destino.
    """
    caminho =[]
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = rot[atual]
    return caminho[::-1]