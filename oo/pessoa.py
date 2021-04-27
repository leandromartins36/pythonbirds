class Pessoa:
    olhos = 2
    def __init__(self,*filhos,nome = None, idade = 41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f'Olá! Meu nome é:  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 41
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_casse = super().cumprimentar()
        return f'{cumprimentar_da_casse}.Aperto de mão'

class Mutante(Pessoa):
    olhos = 5
if __name__ == '__main__':
    leandro = Pessoa(nome = 'Leandro')
    luciano = Pessoa(nome='Luciano')
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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    print(leandro.olhos)
    leandro = Homem(nome='Leandro')
    luciano = Homem(nome='Luciano')
    print(leandro.cumprimentar())
    print(luciano.cumprimentar())















