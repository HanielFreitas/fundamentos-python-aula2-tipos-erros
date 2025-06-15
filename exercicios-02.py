# Números de Ponto Flutuante (float)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

def titulo(titulo):
    print("\n" + titulo.upper())
    print("*" * len(titulo) + "\n")

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
titulo("Soma de Dois números quebrados(float)")
num1 = float(input("Digite um número quebrado: "))
num2 = float(input("Digite outro número quebrado: "))
soma = num1 + num2
print(f"A soma de {num1} + {num2} é igual: {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
titulo("VAMOS CALCULAR SUA MEDIA PARA SABER SE PASSOU OU REPROVOU? ")

n = int(input("Quantas notas você tem para lançar? "))#Perguntando do usuário quantas notas ele precisa calcular
if n == 1:
    print("Não é necessário calcular a média pois só existe uma nota")
else:
    quantidade = []#Criando uma variavel vazia do tipo lista para receber os valores
    
    for i in range(n): #criando um for e passando o range da quantidade de notas

        num = float(input(f'Digite a nota 0{i+1}: '))
        quantidade.append(num)

    media = sum(quantidade) / len(quantidade)
    media_final = 6

    if media < media_final:
        print(f"\nMédia final: {media:.2f}"
        f"\nMédia final menor que {media_final}"
        "\nVocê precisa estudar mais")
    else:
                    print(f"\nMédia final: {media:.2f}"
        f"\nMédia final maior que {media_final}"
        "\nParabéns você passou")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
titulo("VAMOS CALULAR A POTENCIA DE UM NÚMERO")

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print(f"Vamos calular a potencia com a base {base} e o expoente {expoente}."
f"\nO valor da potencia é igual a {potencia}")
    
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
titulo("CONVERTENDO DE Celsius PARA Fahrenheit")

c = float(input("Digita a temperatura em graus Celsius: "))
const1 = 32
const2 = 9/5
Fahrenheit = (c * const2) + const1
print(f"A temperatura de {c:.2f} graus Celsius convertida para Fahrenheit é de {Fahrenheit:.2f} graus Fahrenheit")
