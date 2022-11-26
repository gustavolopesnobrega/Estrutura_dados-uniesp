

def TPilha(vetor):
    stack = []

    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] % 2 == 0:
                stack.append(vetor[i])
            else:
                if len(stack) > 0:
                    continue

        for i in range(len(stack)):
            print(stack.pop(0))


x = TPilha([2, 6, 12, 22, 60, 62, 78, 89, 98, 100, 30, 49, 51, 67, 70])