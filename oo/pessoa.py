class Pessoa:
    olhos = 2
    def __init__(self,*filhos,nome = None, idade = 41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f'ola {id(self)}'


if __name__ == '__main__':
    leandro = Pessoa(nome = 'Leandro')
    luciano = Pessoa(leandro,nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Martins'
    del luciano.filhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(leandro.__dict__)
    print(Pessoa.olhos)
    print(leandro.olhos)









