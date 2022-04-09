from numpy import true_divide
import gerar


print("-=" * 30, "xXx", "=-" * 30)
print("Olá, bem vindo ao RandomSims.\n")
Sims = []

def ProcurarSim(pesquisa):
    print("-=" * 30, "xXx", "=-" * 30)
    achou_ = False
    print(f'{"Nome":<16}{"Sobrenome":<16}{"Idade":<8}{"Cor Cabelo":<22}{"Cor Olhos":<20}{"Altura":<8}{"Emprego":<12}\n')
    for x in Sims:
        if str(pesquisa).isdigit() == True and int(pesquisa) == x.idade:
            achou_ = True
            pass
        elif pesquisa == x.nome.lower() or pesquisa == x.genero.lower():
            achou_ = True
            pass
        else:
            continue
        
        print(f'{x.nome:<16}{x.sobrenome:<16}{x.idade:<8}{x.cor_cabelo:<22}{x.cor_olhos:<20}{x.altura + "m":<8}{x.emprego["nome"]:<10}')

    if achou_ == False:
        print("nada encontrado!!")
    print("-=" * 30, "xXx", "=-" * 30)

def Lersim():
    while True:
        r = input("Qual você deseja ler?").lower()
        if(r == "stop"):
            break
        
        ProcurarSim(r)
        






while True:
    r = input("Você deseja criar ou ler?\n").lower()
    if(r == "stop"):
        break
    if(r == "criar"):
        Sims = gerar.GerarSims()
        print("Criados com sucesso!")
    elif(r == "ler todos"):
        gerar.print_lista(Sims)
    elif(r == "ler sim"):
        Lersim()
    else:
        print("!!ERRO!!")

    

