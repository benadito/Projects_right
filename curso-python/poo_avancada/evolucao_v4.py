class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        # Atributo que pertence a instância
        self.nome = nome
        self._idade = None


    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade


    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + (tuple(f'Homo {adj}' for adj in adjetivos))


    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


jose = HomoSapiens('José')
jose.idade = 20
print(f'Nome: {jose.nome} Idade: {jose.idade}')

