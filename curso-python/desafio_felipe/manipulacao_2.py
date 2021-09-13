import csv
import psycopg2


def read_csv_file_and_insert_into_a_list(file_name):
    all_data = []

    with open(file_name) as entrada:
        dados = csv.reader(entrada)
        for dado in dados:
            all_data.append(dado)

    return all_data


def proccess_registers_into_dict_and_return_a_list(all_data):
    all_data_proccessed = []
    template_dict = {'Index': '', 'Height': '', 'Weight': ''}

    for registro in all_data[1:]:
        template_dict['Index'] = registro[0]
        template_dict['Height'] = registro[1]
        template_dict['Weight'] = registro[2]
        all_data_proccessed.append(dict(template_dict))

    return all_data_proccessed


def print_each_element_in_a_list(list_of_elements):
    for element in list_of_elements:
        print(element)


read = read_csv_file_and_insert_into_a_list('hw_200.csv')
proccess_registers = proccess_registers_into_dict_and_return_a_list(read)
# print_each_element_in_a_list(proccess_registers)

def insert_data_into_db(list_of_elements):
    conn = psycopg2.connect("host=localhost port=5433 user=postgres password=1234")
    cursor = conn.cursor()
    
    for element in list_of_elements: 
        cursor.execute(f"""
            INSERT INTO hw_200 values({element['Index']}, {element['Height']}, {element['Weight']});
        """)
        conn.commit()
    cursor.execute("""
        SELECT * FROM hw_200;
    """)
    result = cursor.fetchall()
    print(result)

insert_data_into_db(proccess_registers)
