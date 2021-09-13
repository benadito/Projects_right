#  Implementação simplificada do map

def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)

print(list(mapear(lambda x: x ** 2, [2, 3, 4])))


def somar(soma, lista):
    for numero in lista:
        yield soma(numero)


print(list(somar(lambda y: y + 2, [2, 3, 4])))