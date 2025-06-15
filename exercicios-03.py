# Strings (str)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

def titulo(titulo):
    print("\n" + titulo.upper())
    print("*" * len(titulo) + "\n")

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
titulo("Vamos colocar seu nome em caixa alta")
nome = input("Digite seu nome que colocamos em caixa alta: ")
print(nome.upper())
