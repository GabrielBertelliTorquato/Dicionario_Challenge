# 8. Ordenação de Dicionário por Valor
# Ordene um dicionário com base nos valores, em ordem decrescente.

def ordenar_dicionario_por_valor(dicionario):
    dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
    return dicionario_ordenado
