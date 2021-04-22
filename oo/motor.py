class Motor:
    def __init__(self ):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
        # if self.velocidade >1:
        #     self.velocidade -= 2
        # elif self.velocidade == 1:
        #     self.velocidade -=1

##testando o Motor

motor = Motor()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)