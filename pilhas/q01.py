
import numpy as np
def maior_numero(stack):
    maior = stack[0]
    for i in range(len(stack)):
        if stack[i] > maior:
            maior = stack[i]
    return maior


numero = maior_numero([1000, 435, 576, 12, 9])
print(numero)