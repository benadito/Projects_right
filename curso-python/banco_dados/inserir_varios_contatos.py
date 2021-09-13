from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES ( %s, %s)'
args = (
    ('Ana', '96765-4321'),
    ('Bia', '95765-4321'),
    ('Luca', '94765-4321'),
    ('Lu', '93765-4321'),
    ('Gui', '92765-4321'),
    ('Beca', '91765-4321'),
    ('Pedro', '99765-4321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg} ')
    else: 
        print(f'Foram incluídos {cursor.rowcount} Registro!')
