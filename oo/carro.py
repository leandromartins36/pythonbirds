
from direcao import Direcao
from motor import Motor

class Carro():
    def __init__(self, direcao, motor ):
        self.direcao  = direcao
        self.motor = motor
    def calcular_velocidade(self):
       return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()



    #testando o Carro

if __name__ == '__main__':

    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.girar_a_direita()
    print(carro.calcular_direcao())

    carro.frear()
    print(carro.calcular_velocidade())

    carro.girar_a_direita()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())