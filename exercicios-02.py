# Números de Ponto Flutuante (float)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

def titulo(titulo):
    print("\n" + titulo.upper())
    print("*" * len(titulo) + "\n")

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
titulo("Soma de Dois números quebrados(float)")
num1 = float(input("Digite um número quebrado: "))
num2 = float(input("Digite outro número quebrado: "))
soma = num1 + num2
print(f"A soma de {num1} + {num2} é igual: {soma}")

