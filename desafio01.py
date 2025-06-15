# Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))
    operador = input("Digite o operador (+, -, *, /): ")

    if operador == '+':
        soma = num1 + num2
    elif operador == '-':
        soma = num1 - num2
    elif operador == '*':
        soma = num1 * num2
    elif operador == '/':
        soma = num1 / num2
    else:
        print("Operador inválido")
    print(soma)

except ZeroDivisionError:
    print('division by zero')
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")