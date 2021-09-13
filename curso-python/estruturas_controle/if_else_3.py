def faixaSalarial(salario):
    if salario in range(0, 900):
        return 'Classe E'
    elif salario in range(901, 2000):
        return 'Classe D'
    elif salario in range(2001, 3050):
        return 'Classe C'
    elif salario in range(3051, 5000):
        return 'Classe B'
    elif salario in range(5001, 10000):
        return 'Classe A'


for salario in (200, 950, 2050, 4000, 5005, 6000):
    print(f'Salario {salario}: {faixaSalarial(salario)}')
