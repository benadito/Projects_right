class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"
    VERDE = "\033[1;32m"


def calcula_media(nota1, nota2):
    media = (nota1+nota2)/2
    return media


while True:
    try:
        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input('Informe a segunda nota: '))
        if (nota1 < 0 or nota1 > 100) or (nota2 < 0 or nota2 > 100):
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print(TerminalColor.ERRO, "Valor inválido:", e,
              TerminalColor.NORMAL)
    else:
        break

media = calcula_media(nota1, nota2)


if media >= 60.0:
    print(TerminalColor.VERDE, 'Você está aprovado na disciplina!',
          TerminalColor.NORMAL)
    print(TerminalColor.VERDE, f'Sua media na disciplina foi de {media}',
          TerminalColor.NORMAL)
else:
    print(TerminalColor.ERRO, 'Você está reprovado!', TerminalColor.NORMAL)
    print(TerminalColor.ERRO, 'Você não alcançou a nota necessaria para')
    print(TerminalColor.ERRO, 'ser aprovado.', TerminalColor.NORMAL)
