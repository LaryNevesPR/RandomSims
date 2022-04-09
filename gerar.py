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
    empregos = Recursos.Recursoss.Ler_Json("Empregos.json")
    count = 0
    while count < 100:
        novo_Sim = Pessoa()
        novo_Sim.cor_cabelo = random.choice(cor_cabelos)
        if random.randint(0,1) == 1:
            novo_Sim.nome = random.choice(nomes_masculinos)
            novo_Sim.genero = "Masculino"
            novo_Sim.altura = random.uniform(1.6,1.95)
        else:
            novo_Sim.nome = random.choice(nomes_femininos)
            novo_Sim.genero = "Feminino"
            novo_Sim.altura = random.uniform(1.48,1.79)
        novo_Sim.idade = random.randint(16, 64)
        novo_Sim.cor_olhos = random.choice(cor_olhos)
        novo_Sim.sobrenome = random.choice(sobrenomes)
        novo_Sim.emprego = random.choice(empregos)
        fomarted_altura = "{:.2f}".format(novo_Sim.altura)
        novo_Sim.altura =  fomarted_altura

    










        Sims.append(novo_Sim)
        count+=1
    return Sims

def print_lista(lista):
    print("-=" * 30, "xXx", "=-" * 30)
    count = 1
    max = 1
    totalid = 0
    maiorsecen =0
    maiorquarenta= 0
    maiorvinte = 0
    menorvinte = 0
    print(f'{"No.":<6}{"Nome":<16}{"Sobrenome":<16}{"Idade":<8}{"Cor Cabelo":<22}{"Cor Olhos":<20}{"Altura":<8}{"Emprego":<12}\n')
    for x in lista:
        print(f'{count:<6}{x.nome:<16}{x.sobrenome:<16}{x.idade:<8}{x.cor_cabelo:<22}{x.cor_olhos:<20}{x.altura + "m":<8}{x.emprego["nome"]:<10}')
        count+=1
        max+=1
        if x.idade >= 60:
            maiorsecen += 1
        elif x.idade >= 40:
            maiorquarenta += 1
        elif x.idade >= 20:
            maiorvinte +=1
        else:
            menorvinte +=1
        totalid+= x.idade
        if max == 20:
            print("-=" * 30, "xXx", "=-" * 30)
            print(f'{"No.":<6}{"Nome":<16}{"Sobrenome":<16}{"Idade":<8}{"Cor Cabelo":<22}{"Cor Olhos":<20}{"Altura":<8}{"Emprego":<12}')
            print("-=" * 30, "xXx", "=-" * 30)
            max = 0
    print("-=" * 30, "xXx", "=-" * 30)
    media = totalid/100
    print(f"     => Maiores que 60 anos = {maiorsecen}")
    print(f"     => Maiores que 40 anos = {maiorquarenta}")
    print(f"     => Maiores que 20 anos = {maiorvinte}")
    print(f"     => Menores que 20 anos = {menorvinte}")
    print(f"A média de idades é {media} anos")


