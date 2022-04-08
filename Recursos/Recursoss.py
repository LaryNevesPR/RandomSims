import os
import json

os.chdir("./Componentes")

def Ler_Nomes(Arquivo):
    Nomes = {}

    if os.path.exists(Arquivo):
        f = open(Arquivo, 'r', encoding='utf-8')
        Nomes = f.read().splitlines()
        f.close()
    return Nomes
