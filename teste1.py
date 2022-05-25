class Pessoa:

    ano = 2022

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento='fruta'):
        if self.comendo:
            print(f'{self.nome} já está comendo!!')
            return
        else:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer!')
            self.comendo = False
            return

    def falar(self, fala):
        if self.comendo:
            print(
                f'{self.nome} não pode comer enquanto fala!\n é falta de educação! ')
            return
        else:
            print(f'{self.nome} disse: "{fala}"')
            print(f'{self.nome} agora está falando!')
            self.falando = True

    def QntAno(self):
        print(f'{self.nome} tem {self.idade} anos.')

    def ano_nascimento(self):
        print(self.ano - self.idade)
