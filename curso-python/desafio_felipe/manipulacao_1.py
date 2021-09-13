import csv

all_data = []

with open('hw_200.csv') as entrada:
    dados = csv.reader(entrada)
    for dado in dados:
        all_data.append(dado)
template_dict = {'Index': '', 'Height': '', 'Weight': ''}
all_data_proccessed = []

for registro in all_data[1:]:
    template_dict['Index'] = registro[0]
    template_dict['Height'] = registro[1]
    template_dict['Weight'] = registro[2]
    all_data_proccessed.append(dict(template_dict))

for data in all_data_proccessed:
    print(data)
