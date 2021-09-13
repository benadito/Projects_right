def get_tipo_ali(ali):
    alis = {
        (1, 9): 'Maça',
        tuple(range(2, 9)): 'Banana',
    }
    ali_escolhido = (tipo for refei, tipo in alis.items() if ali in refei)
    return next(ali_escolhido, '** alimento errado** ')


for ali in range(0, 10):
    print(f'{ali}:  {get_tipo_ali(ali)}')
