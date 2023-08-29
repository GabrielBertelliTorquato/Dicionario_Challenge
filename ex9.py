# 9. Dicionário de Matrizes
# Crie um dicionário de matrizes, onde as chaves são coordenadas e os valores são
# os elementos correspondentes.

def criar_dicionario_matrizes(coordenadas, elementos):
    dicionario_matrizes = {}
    for i in range(len(coordenadas)):
        dicionario_matrizes[coordenadas[i]] = elementos[i]
    
    return dicionario_matrizes
