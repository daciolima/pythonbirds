class Pessoa:

    # Definição de atribudo de classe, geralmente é criado quando se tem um atributo que
    # que terá um valor comum para todos os objetos vindos da classe
    olhos = 2

    # Definição de atributo de instância ou de objeto são realizados no construtor do Objeto
    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 'Olá, eu sou um método estático'

    # Métodos para retornar informações sobre a class
    @classmethod
    def nome_atributos_de_classe(cls):
        return f'O nome da classe é {cls} e contém um atributo chamado {cls.olhos}'


if __name__ == '__main__':
    isaac = Pessoa(nome='Isaac', idade=2)
    dacio = Pessoa(isaac, nome='Dácio Lima', idade=40)
    # Para executar metodo de classe atrelado ao objeto deve-se colocar dessa forma:
    print(dacio.cumprimentar())
    # Caso contrário deve-se passa o objeto como parâmetro.
    print(Pessoa.cumprimentar(dacio))
    print(id(dacio))
    print(dacio.cumprimentar())
    print(dacio.nome)
    print(dacio.idade)
    print(dacio.filhos)
    isaac.sobrenome = 'Lima'
    for filho in dacio.filhos:
        print(f'Nome: {filho.nome} {filho.sobrenome}, idade: {filho.idade}')

    # Exibindo atributo de instância atraves do método __dict__
    print(dacio.__dict__)
    print(isaac.__dict__)
    del isaac.sobrenome
    dacio.olhos = 1
    print(dacio.__dict__)
    print(isaac.__dict__)
    Pessoa.olhos = 3
    print(f'Os objetos da classe Pessoa tem {Pessoa.olhos} olhos.')
    print(f'O Objeto dacio tem {dacio.olhos} olhos.')
    print(id(Pessoa.olhos), id(dacio.olhos), id(isaac.olhos))

    # Método estático pode ser usado pela própria classe como também pelo objeto
    print(Pessoa.metodo_estatico(), dacio.metodo_estatico())
    # Método de classe pode ser usado pela própria classe como também pelo objeto
    print(Pessoa.nome_atributos_de_classe(), '\n' + dacio.nome_atributos_de_classe())

