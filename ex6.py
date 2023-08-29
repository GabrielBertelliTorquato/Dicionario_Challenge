# 6. Compressão de Dicionário
# Comprima um dicionário removendo chaves com valores menores que um
# determinado limite.

def comprimir_dicionario(dicionario, limite):
    dicionario_comprimido = {chave: valor for chave, valor in dicionario.items() if valor >= limite}
    return dicionario_comprimido
