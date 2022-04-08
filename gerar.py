import imp
from os import rename
import random
from Pessoa import Pessoa
import Recursos.Recursoss

Sims = []
def GerarSims():
    nomes_masculinos = Recursos.Recursoss.Ler_Nomes("NomesMasculinos.txt")
    nomes_femininos = Recursos.Recursoss.Ler_Nomes("NomesFemininos.txt")
    cor_cabelos = Recursos.Recursoss.Ler_Nomes("CorCabelos.txt")
    cor_olhos = Recursos.Recursoss.Ler_Nomes("CorOlhos.txt")
    sobrenomes = Recursos.Recursoss.Ler_Nomes("Sobrenomes.txt")
    count = 0
    while count < 500:
        novo_Sim = Pessoa()
        novo_Sim.cor_cabelo = random.choice(cor_cabelos)
        if random.randint(0,1) == 1:
            novo_Sim.nome = random.choice(nomes_masculinos)
            novo_Sim.genero = "Masculino"
        else:
            novo_Sim.nome = random.choice(nomes_femininos)
            novo_Sim.genero = "Feminino"

        novo_Sim.cor_olhos = random.choice(cor_olhos)
        novo_Sim.sobrenome = random.choice(sobrenomes)

    










        Sims.append(novo_Sim)
        count+=1
    return Sims

def print_lista(lista):
    print("-=" * 30, "xXx", "=-" * 30)
    count = 1
    max = 1
    print(f'{"No.":<6}{"Nome":<16}{"Sobrenome":<16}{"Cor Cabelo":<8}{"Cor Olhos":>21}\n')
    for x in lista:
        print(f'{count:<6}{x.nome:<16}{x.sobrenome:<16}{x.cor_cabelo:<22}{x.cor_olhos:<20}')
        count+=1
        max+=1
        if max == 20:
            print("-=" * 30, "xXx", "=-" * 30)
            print(f'{"No.":<6}{"Nome":<16}{"Sobrenome":<16}{"Cor Cabelo":<8}{"Cor Olhos":>21}')
            print("-=" * 30, "xXx", "=-" * 30)
            max = 0
    print("-=" * 30, "xXx", "=-" * 30)




def ler_Arquivos():
    nomes_masculinos = Recursos.Recursoss.Ler_Nomes("NomesMasculinos.txt")
    nomes_femininos = Recursos.Recursoss.Ler_Nomes("NomesFemininos.txt")
    cor_cabelos = Recursos.Recursoss.Ler_Nomes("CorCabelos.txt")
    sobrenomes = Recursos.Recursoss.Ler_Nomes("Sobrenomes.txt")
    print("aa")
