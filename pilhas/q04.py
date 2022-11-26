
import numpy as np


class Street:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimo_carro = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __rua_cheia(self):
        if self.ultimo_carro == self.capacidade - 1:
            return True

        else:
            return False

    def rua_vazia(self):
        if self.ultimo_carro == -1:
            return True

        else:
            return False

    def estacionar(self, placa):
        if self.__rua_cheia():
            print("Rua cheia!")

        else:
            self.ultimo_carro += 1
            self.valores[self.ultimo_carro] = placa

    def retirar(self):
        if self.rua_vazia():
            print("Pilha vazia!")
            return -1

        else:
            valor = self.valores[self.ultimo_carro]
            self.ultimo_carro -= 1
            return valor

    def ver_ultimo_carro(self):
        if self.ultimo_carro != -1:
            return self.valores[self.ultimo_carro]
        else:
            return -1

    def verificar_placa(self, placa):
        if self.rua_vazia():
            return False

        else:
            if placa in self.valores:
                for i in range(self.ultimo_carro + 1):
                    if placa == self.valores[i]:
                        global posicao_carro
                        posicao_carro = i
                        break

                carros_retirar = self.ultimo_carro - posicao_carro
                print(
                    f"É necessário retirar {carros_retirar} carro(s) para o veículo de placa {placa} sair!")
                return True
            else:
                return False


if __name__ == "__main__":
    c = Street(5)
    c.estacionar(5987)
    c.estacionar(5678)
    c.estacionar(4343)
    c.estacionar(2356)
    c.estacionar(6547)
    print(c.verificar_placa(4343))