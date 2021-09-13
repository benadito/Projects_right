def dias_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    return dias.get(dia, '**inválido**')


if __name__ == '__main__':
    for dia in range(1, 8):
        if dia == 1 or dia == 7:
            print(f'{dias_semana(dia)} é final de semana!')
        else:
            print(f'{dias_semana(dia)} é dia de semana!')
