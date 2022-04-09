import gerar

print("-=" * 30, "xXx", "=-" * 30)
print("Olá, bem vindo ao RandomSims.\n")

Sims = []
while True:
    r = input("Você deseja criar ou ler?\n").lower()
    if(r == "stop"):
        break
    if(r == "criar"):
        Sims = gerar.GerarSims()
        print("Criados com sucesso!")
    elif(r == "ler"):
        gerar.print_lista(Sims)
    else:
        print("!!ERRO!!")

    
