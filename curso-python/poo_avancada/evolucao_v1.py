class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        # Atributo que pertence a instância
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
    
jose = Humano('José')
grokn = Humano ('Grokn').das_cavernas()

print(f'Humano.especie: {Humano.especie}')
print(f'Jose.especie: {jose.especie}')
print(f'grokn.especie: {grokn.especie}')