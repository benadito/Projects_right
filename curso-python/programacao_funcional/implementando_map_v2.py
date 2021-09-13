#  Implementação simplificada do map

def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)

print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
