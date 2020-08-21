class Pessoa:
    # Definição de atributo de instância ou de objeto são realizados no construtor do Objeto
    def __init__(self, nome=None, idade=40):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Dácio Lima')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)

