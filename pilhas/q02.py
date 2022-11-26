def equalStack(stack1, stack2):
    if stack1 == stack2:
        return True
    else:
        return False


primeiraStack = equalStack([88, 89, 90, 91], [88, 89, 90])
segundaStack = equalStack([-1, -2, -4], [-1, -2, -4])
print(primeiraStack)
print(segundaStack)