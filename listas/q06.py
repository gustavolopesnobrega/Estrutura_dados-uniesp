import numpy as np


class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.itens = np.empty(self.capacidade, dtype=int)

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.itens[i]:
                return i
        return -1

    def visualizarLista(self):
        print(self.itens)

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('A lista está cheia')
        else:
            self.ultima_posicao += 1
            self.itens[self.ultima_posicao] = valor

    def deletar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.itens[i]:
                posicao = i
                if posicao == -1:
                    return -1
                else:
                    for i in range(posicao, self.ultima_posicao):
                        self.itens[i] = self.itens[i + 1]

                    self.ultima_posicao -= 1
                    print("Item removido com sucesso!")

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"A posição {i} recebeu o item {self.itens[i]}")
