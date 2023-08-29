# 7. Frequência de Palavras em Texto
# Conte a frequência de cada palavra em um texto usando um dicionário.

def frequencia_palavras(texto):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    
    return frequencia
