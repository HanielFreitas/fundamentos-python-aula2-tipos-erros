"""
Inteiros (int)
1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""
# Exercicio 1: Soma de dois números inteiros
print("\nVAMOS TREINAR SOMA DE DOIS NUMEROS INTEIROS?")
print("************************************************\n")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = num1 + num2
print(f"A soma dos números é: {soma}")


# Exercicio 2: Resto da divisão
print("\nVAMOS TREINAR DIVISÃO E SABER QUAL O RESTO DA DIVISÃO?")
print("************************************************\n")
constante = 5
num3 = int(input("Digite um número que o diviremos por 5: "))
resto = num3 % constante
print(f"O resto da divisão de {num3} por {constante} é: {resto}")
