class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
print(d1)


d2  = Data(dia = 7, ano=2022, mes=12)
d2.dia=7
print(d2)
