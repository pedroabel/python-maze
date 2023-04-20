import numpy as np

# Definindo a matriz
print("Matriz:")
i = int(input("Digite o tamanho da dimensão da linha: "))
j = int(input("Digite o tamanho da dimensão da coluna: "))
k = int(input("Digite o tamanho da dimensão da profundidade: "))

matriz = np.zeros((i, j, k))

print("\nOrigem:")
i_origem = int(input("Digite o local da linha: "))
j_origem = int(input("Digite o local da coluna: "))
k_origem = int(input("Digite o local da profundidade: "))

print("\nDestino:")
i_destino = int(input("Digite o local da linha: "))
j_destino = int(input("Digite o local da coluna: "))
k_destino = int(input("Digite o local da profundidade: "))

# Definindo o ponto inicial e final
origem = (i_origem, j_origem, k_origem)
destino = (i_destino, j_destino, k_destino)

# Definindo a função heurística (distância Manhattan


def distancia_heuristica(origem, destino):
    return abs(origem[0] - destino[0]) + abs(origem[1] - destino[1]) + abs(origem[2] - destino[2])

# Definindo a função para encontrar o menor caminho


def a_estrela(matriz, origem, destino):

    # Definindo os nós abertos fechados , custos dos nós e parentes dos nós
    lista_aberta = set([origem])
    lista_fechada = set([])

    custo_lista = {}
    custo_lista[origem] = 0

    parentes = {}
    parentes[origem] = origem

    # Enquanto existir nó aberto
    while len(lista_aberta) > 0:

        ponto_atual = None
        custo_atual = None

        # Definição de custo do ponto atual
        for ponto in lista_aberta:
            if ponto_atual == None or custo_lista[ponto] + distancia_heuristica(ponto, destino) < custo_atual:
                ponto_atual = ponto
                custo_atual = custo_lista[ponto] + \
                    distancia_heuristica(ponto, destino)

        # Se encontrar o objetivo, retorne o caminho
        if ponto_atual == destino:
            caminho = []
            while parentes[ponto_atual] != ponto_atual:
                # Coloca os pontos adicionandos na variavel parentes na variavel caminho
                caminho.append(ponto_atual)
                ponto_atual = parentes[ponto_atual]
            # Reverter o caminho para origem ao destino
            caminho.append(origem)
            caminho.reverse()
            return caminho

        # Senão, continue a busca
        lista_aberta.remove(ponto_atual)
        lista_fechada.add(ponto_atual)

        for vizinho in [
            # x, y, z

            # CENTROS
            (0, 1, 0),
            (0, -1, 0),
            (1, 0, 0),
            (-1, 0, 0),
            (0, 0, 1),
            (0, 0, -1),
            # MEIOS
            (1, 1, 0),
            (-1, -1, 0),
            (1, -1, 0),
            (-1, 1, 0),
            (0, 1, 1),
            (0, -1, -1),
            (0, 1, -1),
            (0, -1, 1),
            (1, 0, 1),
            (-1, 0, -1),
            (1, 0, -1),
            (-1, 0, 1),
            # CANTOS
            (-1, -1, -1),
            (-1, -1, +1),
            (-1, +1, -1),
            (-1, +1, +1),
            (+1, -1, -1),
            (+1, -1, +1),
            (+1, +1, -1),
            (+1, +1, +1),
        ]:
            ponto = (ponto_atual[0] + vizinho[0], ponto_atual[1] +
                     vizinho[1], ponto_atual[2] + vizinho[2])

            # Confere os limites da matriz
            if ponto[0] < 0 or ponto[0] >= len(matriz) or ponto[1] < 0 or ponto[1] >= len(matriz[0]) or ponto[2] < 0 or ponto[2] >= len(matriz[0][0]):
                continue

            if ponto in lista_fechada:
                continue

            custo = custo_lista[ponto_atual] + 1

            if ponto not in lista_aberta or custo < custo_lista[ponto]:
                custo_lista[ponto] = custo
                parentes[ponto] = ponto_atual
                lista_aberta.add(ponto)

    return None


# Executando o algoritmo A* e imprimindo o caminho encontrado
caminho = a_estrela(matriz, origem, destino)

if caminho:
    print("\nCaminho encontrado: ", caminho)
else:
    print("Não foi possível encontrar um caminho.")
