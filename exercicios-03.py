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
text = input("Digite seu nome que colocamos em caixa alta: ")
print(text.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
titulo("Vamos colocar seu nome em minusculo")
nome = input("Digite seu nome que colocamos em minúsculo: ")
print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
titulo("Vamos tirar os espaços do inicio e do fim da frase")
frase = input("Digite um frase: ")
print(frase.strip())