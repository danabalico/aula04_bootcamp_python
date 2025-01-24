# EXERCICIOS MAIS AVANÇADOS

# 6. Eliminação de Duplicatas
# Dada uma lista de emails, remover todos os duplicados

# emails:list = ["jordanabalico@gmail.com", "jordana@123", "joao@joao", "jordanabalico@gmail.com"]
# emails_sem_duplicacao:list = list(set(emails))
# print(emails_sem_duplicacao)


# 7. Filtragem de Dados
# Dada uma lista de idades, filtrar apenas aquelas que são 
# maiores ou iguais a 18.

# idades:list =[18,22,39,0,1,4,2,16,15,10]
# maiores_de_idade = [idade for idade in idades if idade >=18]
# print(maiores_de_idade)

# 8. Ordenação Personalizada
# Dada uma lista de dicionários representando pessoas, 
# ordená-las pelo nome.


# pessoas= [
#     {"nome": "Jordana",
#      "idade": 25,
#      "hobbie": "ler"
#     },

#     {"nome": "joao",
#      "idade": 24,
#      "hobbie": "tecnologia"
#     },

#     {"nome": "Ana",
#      "idade": 2,
#      "hobbie": "brincar"
#     },

#     {"nome": "Maria",
#      "idade":30,
#      "hobbie": "dormir"
#     }
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"].lower())
# for pessoa in pessoas:
#     print(pessoa)


# 9. Agregação de Dados
# Dado um conjunto de números, calcular a média.

# 10. Divisão de Dados em Grupos
# Dada uma lista de valores, dividir em duas listas: 
# uma para valores pares e outra para ímpares.

# Exercícios com Dicionários
# 11. Atualização de Dados
# Dada uma lista de dicionários representando produtos, 
# atualizar o preço de um produto específico.

# 12. Fusão de Dicionários
# Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Dado um dicionário de estoque de produtos, 
# filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Dado um dicionário, criar listas separadas para suas chaves 
# e valores.

# 15. Contagem de Frequência de Itens
# Dada uma string, contar a frequência de cada caractere 
# usando um dicionário.