# 3. Palavras Únicas por Chave
# Dado um dicionário de listas, encontre as palavras que são únicas para cada
# chave.

def palavras_unicas_por_chave(dicionario):
    palavras_unicas = {}
    for chave, lista_palavras in dicionario.items():
        contador_palavras = {}
        for palavra in lista_palavras:
            if palavra in contador_palavras:
                contador_palavras[palavra] += 1
            else:
                contador_palavras[palavra] = 1
        
        palavras_unicas[chave] = [palavra for palavra, contador in contador_palavras.items() if contador == 1]
    
    return palavras_unicas
