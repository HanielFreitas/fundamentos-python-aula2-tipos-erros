# Booleanos (bool)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

def titulo(titulo):
    print("\n" + titulo.upper())
    print("*" * len(titulo) + "\n")

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
titulo("Aqui é uma logica boolena com o AND")
verdade = True
Falso = False
resultado = verdade and Falso
print(f"Resultado do AND lógica: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
titulo("Aqui vamos revelar o resultado dos valores que você colocar com a logica OR")
valor1 = bool(input("Digite True ou False: "))
valor2 = bool(input("Digite True ou False: "))
resultado_user = valor1 or valor2
print(f"Resultado da boolena é: {resultado_user}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
titulo("Aqui vamos inverter o valor booleano")
valor3 = input("Digite True ou False: ").strip().capitalize()
if valor3 == "True":
    bool_value = True
    invertido = not bool_value
    print(invertido)
elif valor3 == "False":
    bool_value = False
    invertido = not bool_value
    print(invertido)
else:
    print("Entrada inválida! Use apenas True ou False")