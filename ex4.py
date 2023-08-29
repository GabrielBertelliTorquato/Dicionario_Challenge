# 4. Aninhamento de Chaves
# Crie um dicionário aninhado com níveis de chaves fornecidos em uma lista.

def criar_dicionario_aninhado(niveis_chaves, valor):
    dicionario = valor
    for nivel in reversed(niveis_chaves):
        dicionario = {nivel: dicionario}
    
    return dicionario
