
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {
        NORTE: OESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
      self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

        #outro modo de girara a direita
        # if self.valor == NORTE:
        #     self.valor = LESTE
        # elif self.valor == LESTE:
        #     self.valor = SUL
        # elif self.valor == SUL:
        #     self.valor = OESTE
        # elif self.valor == OESTE:
        #     self.valor = NORTE

    # outro modo de girara a esquerda
    # def girar_a_esquerda(self):
    #     if self.valor == NORTE:
    #         self.valor = OESTE
    #     elif self.valor == OESTE:
    #         self.valor = SUL
    #     elif self.valor == SUL:
    #         self.valor = LESTE
    #     elif self.valor == LESTE:
    #         self.valor = NORTE

##testando a direção

direcao = Direcao()
print(direcao.valor)
direcao.girar_a_direita()
print(direcao.valor)
direcao.girar_a_direita()
print(direcao.valor)
direcao.girar_a_direita()
print(direcao.valor)
direcao.girar_a_direita()
print(direcao.valor)
direcao.girar_a_esquerda()
print(direcao.valor)
direcao.girar_a_esquerda()
print(direcao.valor)
direcao.girar_a_esquerda()
print(direcao.valor)
direcao.girar_a_esquerda()
print(direcao.valor)

