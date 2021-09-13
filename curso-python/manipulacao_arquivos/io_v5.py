with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if not arquivo.closed:
    print('Arquivo já foi fechado!')
