# Mesclar Dicionários
# Combine dois dicionários, substituindo valores comuns pela soma dos valores
# correspondentes.

pessoas_idade = {
    'Gabriel' :20, 
    'Lucas': 20, 
    'Bruno': 22, 
    'Sid' : 25, 
    'Serrano': 22, 
    'Bianca': 28, 
    'Ricardo': 25, 
    'Ronaldo':  30, 
    'Isak': 40, 
    'Jose': 21
    
}

pessoas = {
    "João": 25,
    "Maria": 30,
    "Pedro": 28,
    "Ana": 22,
    "Carlos": 35,
    "Lúcia": 40,
    "Miguel": 19,
    "Sofia": 27,
    "Rafael": 32,
    "Laura": 24
}

pessoas_idade.update(pessoas)

print (pessoas_idade)