from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce 


# Português dos Brasil, para termos os dias e os meses em PT-BR.
setlocale(LC_ALL, 'pt-BR')


# Listar todos os meses do ano com 31 dias
# 1. (Filter) Pegar os indices de todos os meses com 31 dias, 1, 3, 5.....
#2. (Map) transformar os índices em nomes
#3. (Reduce) Juntar tudo para imprimir

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nomes, 'Meses com 31 dias:')
print(juntar_meses)