import csv


with open('desafio-ibge.csv', encoding='ISO-8859-1') as arquivo:
    dados = arquivo.read()
    for cidade in csv.reader(dados.splitlines()):
        print(f'{cidade[8]}: {cidade[3]}')
