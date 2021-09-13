import csv


def read_csv_file_and_insert_into_a_list(file_name):
    all_data = []
    with open(file_name) as entrada:
        dados = csv.reader(entrada)
        for dado in dados:
            all_data.append(dado)

    return all_data


def proccess_registers_into_dict_and_return_a_list(all_data):
    template_dict = {'FID': '', 'objectid': '', 'cod_origem': '', 'nome_orige': ''}
    all_data_proccessed = []

    for registro in all_data[]:
        template_dict['FID'] = registro[0]
        template_dict['objectid'] = registro[1]
        template_dict['cod_origem'] = registro[2]
        template_dict['nome_orige'] = registro[3]
        all_data_proccessed.append(dict(template_dict))

    return all_data_proccessed

    
def print_each_element_in_a_list(list_of_elements):
    for element in list_of_elements:
        print(element)


read = read_csv_file_and_insert_into_a_list('desafio-ibge.csv')
proccess_registers = proccess_registers_into_dict_and_return_a_list(read)
print_each_element_in_a_list(proccess_registers)
