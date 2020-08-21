class Pessoa:
    # Definição de atributo de instância ou de objeto são realizados no construtor do Objeto
    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    isaac = Pessoa(nome='Isaac', idade=2)
    dacio = Pessoa(isaac, nome='Dácio Lima', idade=40)
    print(Pessoa.cumprimentar(dacio))
    print(id(dacio))
    print(dacio.cumprimentar())
    print(dacio.nome)
    print(dacio.idade)
    print(dacio.filhos)
    for filho in dacio.filhos:
        print(f'Nome: {filho.nome}, idade: {filho.idade}')

