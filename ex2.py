# Maior Valor em Dicionário de Dicionários
# Encontre a chave e valor com o maior valor em um dicionário de dicionários.

def pessoa_mais_velha(dicionario):
    pessoa_mais_velha = max(dicionario, key=lambda pessoa: dicionario[pessoa]['idade'])
    return dicionario[pessoa_mais_velha]

pessoas_idade = {
    'pessoa_1': {'nome': 'Gabriel', 'idade': 22},
    'pessoa_2': {'nome': 'André', 'idade': 25},
    'pessoa_3': {'nome': 'Bruno', 'idade': 32},
    'pessoa_4': {'nome': 'Ana', 'idade': 30},
}

pessoa_mais_velha = pessoa_mais_velha(pessoas_idade)
print(pessoa_mais_velha)