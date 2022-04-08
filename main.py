import gerar

print("-=" * 30, "xXx", "=-" * 30)
print("Olá, bem vindo ao RandomSims.")

Sims = []
while True:
    r = input("Você deseja criar ou ler?").lower()
    if(r == "stop"):
        break
    if(r == "criar"):
        Sims = gerar.GerarSims()
    elif(r == "ler"):
        gerar.print_lista(Sims)
    else:
        print("!!ERRO!!")

    
