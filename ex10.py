# 10. Mapeamento de Palavras
# Crie um dicionário que mapeie palavras em um texto para palavras diferentes com
# base em um dicionário de substituição.

def mapear_palavras(texto, dicionario_substituicao):
    palavras = texto.split()
    texto_mapeado = [dicionario_substituicao.get(palavra, palavra) for palavra in palavras]
    return ' '.join(texto_mapeado)
