

import numpy as np


class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def escolhido(chapeu):
        soldado = [i for i in range(1, chapeu + 1)]
        i = 0
        c = 1
        while len(soldado) > 1:
            if i == len(soldado) - 1:
                print(
                    f'Rodada {c} Sobraram:  {soldado} Eliminado:   {soldado[0]}')
                soldado.pop(0)
                i = 0
                c += 1
            elif i == len(soldado) - 2:
                print(
                    f'Rodada {c} Sobraram:  {soldado} Eliminado:   {soldado[i + 1]}')
                soldado.pop(i + 1)
                i = 0
                c += 1
            else:
                print(
                    f'Rodada {c} Sobraram:  {soldado} Eliminado:   {soldado[i + 1]}')
                soldado.pop(i + 1)
                i += 1
                c += 1
        print(f'\n O soldado escolhido foi o que tem o chapéu : {soldado[i]} ')

    escolhido(4)