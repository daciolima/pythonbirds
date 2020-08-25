"""
Criar classe carro com dois atributos compostos por duas outras classe:

1 - Motor
2 - Direcao

Motor
A classe motor terá a responsabilidade de controlar a velocidade.
Ele oferecerá os seguintes atributos:
1. Atributo de dado(Instância) - Velocidade
2. Método acelerá qie deve era incrementar a velocidade em uma unidade
3. Método desacelerá que deverá decrementar a velocidade em duas unidades

Direcao
A classe Direção terá a responsabilidade de controlar a direção.
Ela terá os seguintes atributos:
1. Valor da direçao com valores possíveis de: Norte, Leste, Sul e Oeste
2. Método girar_direita
3. Método gira_esquerda
    N
  O   L
    S

Exemplo:
# Testando Motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.desacelerar()  # decrementa duas unidades
>>> motor.velocidade
1
>>> motor.desacelerar()  # decrementa duas unidades da velocidade até 0.
>>> motor.velocidade
0

# Testando Direção
>>> direcao = Direcao()
>>> direcao.valor # valor default = 'Norte'
'Norte'
>>> direcao.girar_direita()   # Sequencia> Norte, Leste, Sul, Oeste
>>> direcao.valor
'Leste'

>>> direcao.girar_direita()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Sul'

>>> direcao.girar_direita()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Oeste'

>>> direcao.girar_direita()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Norte'


>>> direcao.girar_esquerda()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Oeste'

>>> direcao.girar_esquerda()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Sul'

>>> direcao.girar_esquerda()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Leste'

>>> direcao.girar_esquerda()   # Sequencia> Norte, Oeste, Sul, Leste
>>> direcao.valor
'Norte'

# Testando o Carro
>>> carro = Carro(motor, direcao) # Valor inicial 0. Calcula do que está vindo dos métodos do motor
>>> carro.calcular_velocidade()
0

>>> carro.desacelerar()
>>> carro.calcular_velocidade()
0

>>> carro.calcular_direcao() # Valor inicial 'Norte'. Calcula o que vier dos métodos da Direcao
'Norte'

>>> carro.girar_direita()
>>> carro.calcular_direcao()
'Leste'

>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
'Norte'

>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""

# Para rodar o Doctest via console: python -m doctest -f <nome_do_arquivo.py>


class Carro:

    # def __init__(self, *args):
    #     self.motor = Motor()
    #     self.direcao = Direcao()

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def desacelerar(self):
        self.motor.desacelerar()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_direita(self):
        self.direcao.girar_direita()

    def girar_esquerda(self):
        self.direcao.girar_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def desacelerar(self):
        self.velocidade -= 2
        # Caso tenha o valor positivo retona positivo, caso negativo, retorna 0.
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Direcao:

    rotacao_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_direita(self):
        self.valor = self.rotacao_direita_dct[self.valor]

    def girar_esquerda(self):
        self.valor = self.rotacao_esquerda_dct[self.valor]
