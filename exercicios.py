#exercicios de listas e dicionários:
# 1.Crie uma lista com os números de 1 a 10 e use um loop 
# para imprimir cada número elevado ao quadrado.

# 2.Dada a lista ["Python", "Java", "C++", "JavaScript"], 
# remova o item "C++" e adicione "Ruby".

# 3.Crie um dicionário para armazenar informações de um livro, 
# incluindo título, autor e ano de publicação. 
# Imprima cada informação.

# 4.Escreva um programa que conta o número de ocorrências 
# de cada caractere em uma string usando um dicionário.

# 5.Dada a lista ["maçã", "banana", "cereja"] e o
# dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.


#resoluçã0
#1.
# lista_de_numeros=list(range(1,11))
# for numero in lista_de_numeros:
#     print(numero**2)

#2.
# lista_de_linguagens:list=["Python", "Java", "C++", "JavaScript"]
# lista_de_linguagens.remove("C++")
# lista_de_linguagens.append("Ruby")
# print(lista_de_linguagens)

#3.
# from typing import Dict
# livro:dict[str, int]= {
#     "Titulo": "Vimos e ouvimos",
#     "Autor": "Israel Subira",
#     "Ano": "2024",
# }

# lista_de_elementos_do_livro:list = livro.items()
# for elemento in lista_de_elementos_do_livro:
#     print(elemento)

#4.
# def contar_caracteres(s): 
#     contagem:dict= {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem
# resultado = contar_caracteres("engenharia de dados")
# for caractere, quantidade in resultado.items():
#     print(f"{caractere}: {quantidade}")

#5.
lista_de_compras:list = ["maçã", "banana", "cereja"]
preco_dos_itens: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preco_total:float = sum(preco_dos_itens[item] for item in lista_de_compras)
print(f"Preço total: {preco_total}")