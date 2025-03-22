# Algoritmos da segunda parte da disciplina de Otimização em Redes

**Aluno:** Pedro Igor de Souza Malaquias

**Professor:** Marco Antonio M Carvalho

**Disciplina:** Otimização em Redes

O objetivo consiste em implementar os algoritmos da sagunda parte da disciplina de Otimização em Redes. Os algoritmos implementados são:
    - Redes de Fluxo, Problema de Fluxo, Formulação;
    - Fluxo Viável, O problema da Circulação viável em Redes;
    - Fluxo Máximo;
    - Algoritmo de Ford-Fulkerson;
    - Algoritmo de Dinitz;
    - Algoritmo de MPM;
    - Fluxo de Custo Mínimo, Algoritmo de Cancelamento de Ciclos;
    - Algoritmo de Caminho Mais Curto Sucessivos;
  
## Especificação de Entrada padrão

A primeira linha da entrada contém quatro inteiros *n*, *m*, *b* e *i*, indicando a quantidade de vértices, a quantidade de arestas/arcos, um valor binário indicando se o grafo é direcionado (valor 1) ou não (valor 0) e um índice do vértice (enumerados de 1 a *n*) a partir do qual será executado o algoritmo.

Em seguida haverá *m* linhas, cada uma contendo três inteiros, indicando o vértice de origem (enumerados de 1 a *n*), o vértice de destino e o peso das arestas/arcos, que podem ser negativos.

### Exemplo de Entrada

4 7 1 1  
1 2 -1  
1 3 1  
1 4 1
2 3 -1  
2 4 1  
3 4 -1
4 1 -1
