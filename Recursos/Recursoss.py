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

def Ler_Json(Arquivo):
    Itens = {}
    if os.path.exists(Arquivo):
        with open(Arquivo, 'r', encoding='utf-8') as f:
            Itens= json.load(f)
    return Itens

