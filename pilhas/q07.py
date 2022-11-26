
def TPilha2(N, P, vetor):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                print(f"numero retirado: {N[len(N)-1]}")
                N.pop()
            if len(P) > 0:
                print(f"numero retirado: {P[len(P) - 1]}")
                P.pop()
        elif vetor[i] > 0:
            P.append(vetor[i])
        else:
            N.append(vetor[i])

    print(f"Os numeros negativos: {N}. Os numeros positivos: {P}")


parametros = TPilha2([], [], [6, -5, 1, 4, -2, -4, 10, 3, -3, 0, -5])