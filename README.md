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

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

. ├── input/ # Arquivos de entrada para os algoritmos
│ ├── input1.txt # Exemplos de grafos para testes
│ ├── input2.txt
│ └── ... # Outros arquivos de entrada
├── src/ # Código-fonte principal
│ ├── main.py # Arquivo principal para execução do programa
│ ├── algorithms/ # Implementação dos algoritmos
│ │ ├── BellmanFord.py
│ │ ├── Dijkstra.py
│ │ ├── FordFulkerson.py
│ │ ├── ...
│ ├── utils/ # Utilitários e funções auxiliares
│ │ ├── readFile.py
│ │ ├── load_graph.py
│ │ ├── exibir_graficamente.py
│ │ └── ...
├── README.md # Documentação do projeto
├── requirements.txt # Dependências do projeto
└── .gitignore # Arquivos ignorados pelo Git

## Como Executar

1. Certifique-se de ter o Python 3.8 ou superior instalado.
2. Instale as dependências do projeto executando:

    ``` bash
        pip install -r requirements.txt
    ```

3. Execute o programa principal:

    ``` bash
        python src/main.py 
    ```

## Dependências

As bibliotecas utilizadas no projeto estão listadas no arquivo ``requirements.txt``. As principais são:

- ``numpy``: Para operações matemáticas.
- ``networkx``: Para manipulação e visualização de grafos.
- ``matplotlib``: Para exibição gráfica dos grafos.
  
### Exemplos de Uso

Exemplo 1: Algoritmo de Dijkstra

Entrada:

```` plaintext
4 6 1 1
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 1
````

Saída:

```` plaintext
Caminho mais curto até 4: 1 → 4
Distância total: 1
````

Exemplo 2: Algoritmo de Fluxo Máximo (Ford-Fulkerson)

Entrada:

```` plaintext
4 5 1 1
1 2 10
1 3 5
2 3 15
2 4 10
3 4 10
````

Saída:

```` plaintext
Fluxo máximo entre 1 e 4: 15
````

## Descrição dos Algoritmos
