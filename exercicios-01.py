"""
Inteiros (int)
1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""
#Adicionando uma função
def titulo(titulo):
    print("\n" + titulo)
    print("*" * len(titulo) + "\n")

try:

    # Exercicio 1: Soma de dois números inteiros
    titulo("VAMOS TREINAR SOMA DE DOIS NUMEROS INTEIROS?")
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    soma = num1 + num2
    print(f"A soma dos números é: {soma}")


    # Exercicio 2: Resto da divisão
    titulo("VAMOS TREINAR DIVISÃO E SABER QUAL O RESTO DA DIVISÃO?")
    constante = 5
    num3 = int(input("Digite um número que o diviremos por 5: "))
    resto = num3 % constante
    print(f"O resto da divisão de {num3} por {constante} é: {resto}")

    # Exercicio 3: Multiplicação de dois números
    titulo("VAMOS TREINAR MULTIPLICAÇÃO DE DOIS NÚMEROS INTEIROS?")
    num4 = int(input("Digite um número inteiro: "))
    num5 = int(input("Digite outro número inteiro: "))
    multi = num4 * num5
    print(f"A multiplicação do {num4} pelo {num5} é igual a {multi}")


    #4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    #Exercicio 4: Divisão de dois numeros inteiro

    titulo("VAMOS TREINAR A DIVISÃO DE DOIS NÚMEROS INTEIROS E SABER QUAL O NOSSO QUOCIENTE?")
    num6 = int(input("Digite um número inteiro: "))
    num7 = int(input("Digite outro número intiro: "))
    divisao = num6 // num7
    print(f"A divisão do {num6} pelo {num7} é igual a: {divisao}")

    #5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
    titulo("VAMOS TREINAR RAIZ QUADRADA AGORA?")
    num8 = int(input("Digite a base: "))
    num9 = int(input("Digite o expoente: "))
    conta = num8 ** num9
    print(
        f"Sendo a base {num8} e o expoente {num9} o resultado é: {conta}."
    f" Pois a base {num8} se repete pela quantidade de vezes do meu expoente {num9}"
    )

except ZeroDivisionError:
    print("integer division or modulo by zero")
except KeyboardInterrupt:
    print("Acredito que você não queira mais digitar nenhum número")