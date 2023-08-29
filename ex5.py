# 5. Dicionário Circular
# Crie um dicionário em que a última chave aponte para a primeira chave.

def criar_dicionario_circular(chaves):
    dicionario = {}
    for i, chave in enumerate(chaves):
        dicionario[chave] = chaves[(i + 1) % len(chaves)]
    
    return dicionario